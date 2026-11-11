from datetime import timedelta
import pytest
from fastapi.testclient import TestClient
from config import settings
from deps import get_current_user, get_user_service
from main import app
from models.auth import TokenPayload, User
from repositories.json_repository import JsonRepository
from services import integration_keys as keys

@pytest.fixture
def env(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "data_dir", tmp_path)
    monkeypatch.setattr(settings, "storage_type", "json")
    user = TokenPayload(sub="owner", username="owner", profile_dir="family", caregiver_id="caregiver")
    repo = JsonRepository(tmp_path / "family")
    repo.create("baby", {"id":"baby", "name":"Baby"})
    class Users:
        def get_by_id(self, uid):
            return User(id="owner", username="owner", display_name="Owner", hashed_password="unused", profile_dir="family", caregiver_id="caregiver") if uid == "owner" else None
    app.dependency_overrides[get_current_user] = lambda: user
    monkeypatch.setattr("routers.integrations.get_user_service", lambda: Users())
    yield TestClient(app), user, repo
    app.dependency_overrides.clear()

def issue(client, grants):
    response = client.post("/api/integrations/keys", json={"name":"Automation", "grants":grants, "expires_at":(keys.now()+timedelta(days=1)).isoformat()})
    assert response.status_code == 201, response.text
    return response.json()

def headers(key):
    return {"Authorization": "Bearer " + key["secret"]}

def event(kind="feeding"):
    return dict(baby_id="baby", caregiver_id="spoof", type=kind, subtype="bottle_formula", timestamp="2026-11-11T14:00:00Z", quantity=150, unit="ml")

def test_hash_only_and_revocation(env):
    client,user,repo=env
    key=issue(client,{"feeding":["read"]})
    stored=keys.KeyStore().get(key["id"])
    assert key["secret"] not in str(stored)
    assert "digest" not in key
    listed=client.get("/api/integrations/keys").json()
    assert "secret" not in listed[0] and "digest" not in listed[0]
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==200
    assert client.delete("/api/integrations/keys/"+key["id"]).status_code==204
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==401

def test_module_and_action_isolation(env):
    client,user,repo=env
    key=issue(client,{"sleep":["read"]})
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==403
    assert client.post("/api/v1/events",json=event("sleep"),headers=headers(key)).status_code==403
    assert client.get("/api/v1/events?event_type=sleep&baby_id=other-family",headers=headers(key)).status_code==404

def test_write_delete_admin_and_attribution(env):
    client,user,repo=env
    key=issue(client,{"feeding":["write"]})
    response=client.post("/api/v1/events",json=event(),headers=headers(key))
    assert response.status_code==201,response.text
    created=response.json()
    assert created["caregiver_id"]=="caregiver"
    eid=created["id"]
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==403
    assert client.patch("/api/v1/events/"+eid,json={"quantity":120},headers=headers(key)).status_code==200
    assert client.patch("/api/v1/events/"+eid,json={"type":"sleep"},headers=headers(key)).status_code==422
    assert client.delete("/api/v1/events/"+eid,headers=headers(key)).status_code==403
    admin=issue(client,{"feeding":["admin"]})
    assert client.delete("/api/v1/events/"+eid,headers=headers(admin)).status_code==204
    assert client.get("/api/v1/events?event_type=sleep&baby_id=baby",headers=headers(admin)).status_code==403

def test_expiration_and_validation(env):
    client,user,repo=env
    assert client.post("/api/integrations/keys",json={"name":"x","grants":{"unknown":["admin"]},"expires_at":(keys.now()+timedelta(days=1)).isoformat()}).status_code==422
    key=issue(client,{"feeding":["read"]})
    stored=keys.KeyStore().get(key["id"])
    stored["expires_at"]=(keys.now()-timedelta(seconds=1)).isoformat()
    keys.KeyStore().save(stored)
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==401

def test_key_is_not_jwt_or_management_credential(env):
    client,user,repo=env
    key=issue(client,{"integrations":["admin"]})
    app.dependency_overrides.clear()
    assert client.get("/api/integrations/keys",headers=headers(key)).status_code==401
    assert client.get("/api/events?baby_id=baby",headers=headers(key)).status_code==401

def test_other_profile_cannot_revoke(env):
    client,user,repo=env
    key=issue(client,{"feeding":["read"]})
    other=TokenPayload(sub="other",username="other",profile_dir="other",caregiver_id="other")
    app.dependency_overrides[get_current_user]=lambda:other
    assert client.get("/api/integrations/keys").json()==[]
    assert client.delete("/api/integrations/keys/"+key["id"]).status_code==404


def test_removed_owner_invalidates_key(env, monkeypatch):
    client,user,repo=env
    key=issue(client,{"feeding":["read"]})
    class Missing:
        def get_by_id(self, uid): return None
    monkeypatch.setattr("routers.integrations.get_user_service",lambda:Missing())
    assert client.get("/api/v1/events?event_type=feeding&baby_id=baby",headers=headers(key)).status_code==401

def test_gcs_store_persists_revocation(env, monkeypatch):
    from google.api_core.exceptions import NotFound
    from google.cloud import storage
    records={}
    class Blob:
        def __init__(self,name): self.name=name
        def upload_from_string(self,data,**kwargs): records[self.name]=data
        def download_as_text(self):
            if self.name not in records: raise NotFound("missing")
            return records[self.name]
    class Bucket:
        def blob(self,name): return Blob(name)
        def list_blobs(self,prefix): return [Blob(k) for k in records if k.startswith(prefix)]
    class Client:
        def bucket(self,name): return Bucket()
    monkeypatch.setattr(storage,"Client",Client)
    monkeypatch.setattr(settings,"storage_type","gcs")
    client,user,repo=env
    key=keys.issue(user,"GCS",{"feeding":["read"]},keys.now()+timedelta(days=1))
    assert keys.authenticate(key["secret"])["id"]==key["id"]
    record=keys.KeyStore().get(key["id"])
    record["revoked"]=True
    keys.KeyStore().save(record)
    from fastapi import HTTPException
    with pytest.raises(HTTPException) as exc: keys.authenticate(key["secret"])
    assert exc.value.status_code==401
