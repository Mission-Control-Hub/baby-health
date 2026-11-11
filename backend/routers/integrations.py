"""Account-managed API keys and a deliberately scoped event API."""
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field, AwareDatetime
from deps import get_current_user, get_user_service, get_profile_repository
from models.auth import TokenPayload
from models.event import EventIncoming, EventUpdate
from services import integration_keys as keys
from services.event_normalization import normalize_event_payload
from services import EventService
from routers.events import create_event, update_event, delete_event

router = APIRouter(prefix="/api/integrations", tags=["integrations"])
api = APIRouter(prefix="/api/v1", tags=["integration-events"])
security = HTTPBearer(scheme_name="IntegrationApiKey", description="API key bhk_… created in Integrations")

class KeyCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80, pattern=r".*\S.*")
    grants: dict[str, list[str]]
    expires_at: AwareDatetime

@router.get("/keys")
def list_keys(user: TokenPayload = Depends(get_current_user)):
    return [keys.public(k) for k in keys.KeyStore().records() if k["profile_dir"] == user.profile_dir and k["owner_id"] == user.sub]

@router.get("/modules")
def modules(user: TokenPayload = Depends(get_current_user)):
    return {"modules": keys.MODULES, "actions": keys.ACTIONS}

@router.post("/keys", status_code=201)
def create_key(body: KeyCreate, user: TokenPayload = Depends(get_current_user)):
    return keys.issue(user, body.name.strip(), body.grants, body.expires_at)

@router.delete("/keys/{key_id}", status_code=204)
def revoke_key(key_id: str, user: TokenPayload = Depends(get_current_user)):
    record = keys.KeyStore().get(key_id)
    if not record or record["profile_dir"] != user.profile_dir or record["owner_id"] != user.sub:
        raise HTTPException(404, "Key not found")
    record["revoked"] = True
    keys.KeyStore().save(record)


def integration_context(cred: HTTPAuthorizationCredentials = Depends(security)):
    record = keys.authenticate(cred.credentials)
    user = get_user_service().get_by_id(record["owner_id"])
    if not user or user.profile_dir != record["profile_dir"] or user.caregiver_id != record["caregiver_id"]:
        raise HTTPException(401, "Credential owner no longer has access")
    principal = TokenPayload(sub=user.id, username=user.username, profile_dir=user.profile_dir, caregiver_id=user.caregiver_id)
    return record, principal, get_profile_repository(principal)

EVENT_MODULES = {"feeding":"feeding", "hydration":"hydration", "sleep":"sleep", "diaper":"diapers", "activity":"activities", "health":"health", "bath":"activities"}

def module_for(event_type):
    module = EVENT_MODULES.get(event_type)
    if not module:
        raise HTTPException(422, "Unsupported event type")
    return module

def existing(repo, event_id):
    event = repo.get_by_id("event", event_id)
    if not event:
        raise HTTPException(404, "Event not found")
    return event

@api.get("/events")
def list_integration_events(event_type: str, baby_id: str, ctx=Depends(integration_context)):
    record, user, repo = ctx
    keys.require(record["grants"], module_for(event_type), "read")
    if not repo.get_by_id("baby", baby_id):
        raise HTTPException(404, "Baby not found")
    return repo.get_all("event", baby_id=baby_id, type=event_type)

@api.post("/events", status_code=201)
async def create_integration_event(body: EventIncoming, ctx=Depends(integration_context)):
    record, user, repo = ctx
    try:
        normalized = normalize_event_payload(body.model_dump())
    except ValueError as exc:
        raise HTTPException(422, str(exc)) from exc
    keys.require(record["grants"], module_for(normalized["type"]), "write")
    if not repo.get_by_id("baby", body.baby_id):
        raise HTTPException(404, "Baby not found")
    body.caregiver_id = user.caregiver_id
    return await create_event(body, EventService(repo))

@api.patch("/events/{event_id}")
async def update_integration_event(event_id: str, body: EventUpdate, ctx=Depends(integration_context)):
    record, user, repo = ctx
    current = existing(repo, event_id)
    keys.require(record["grants"], module_for(current["type"]), "write")
    # A patch must not move an event into a forbidden module or alter attribution.
    payload = body.model_dump(exclude_unset=True)
    if any(k in payload for k in ("type", "baby_id", "caregiver_id")):
        raise HTTPException(422, "Event type, baby and attribution are immutable")
    return await update_event(event_id, body, EventService(repo))

@api.delete("/events/{event_id}", status_code=204)
async def delete_integration_event(event_id: str, ctx=Depends(integration_context)):
    record, user, repo = ctx
    event = existing(repo, event_id)
    keys.require(record["grants"], module_for(event["type"]), "delete")
    await delete_event(event_id, EventService(repo))
