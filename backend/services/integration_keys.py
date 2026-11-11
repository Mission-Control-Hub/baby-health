"""API keys: hashed secrets, per-key persistence, and module grants."""
from __future__ import annotations
import hashlib
import hmac
import json
import os
import secrets
import uuid
from datetime import datetime, timezone
from fastapi import HTTPException
from config import settings

MODULES = ("feeding", "sleep", "hydration", "diapers", "activities", "growth", "health", "milestones", "caregivers", "profile", "integrations")
ACTIONS = ("read", "write", "delete", "admin")

def now():
    return datetime.now(timezone.utc)

def validate_grants(grants):
    if not grants or any(m not in MODULES or not a or any(x not in ACTIONS for x in a) for m,a in grants.items()):
        raise HTTPException(422, "Invalid or empty module grants")
    return grants

def require(grants, module, action):
    actions = grants.get(module, [])
    if action not in actions and "admin" not in actions:
        raise HTTPException(403, "Insufficient module permission")

class KeyStore:
    # Independent immutable/revocable records avoid lost updates between keys.
    def __init__(self):
        self.path = settings.data_dir / "integration_keys"
        self.bucket = None
        if settings.storage_type == "gcs":
            from google.cloud import storage
            self.bucket = storage.Client().bucket(settings.gcs_bucket)

    def save(self, record):
        key = record["id"]
        raw = json.dumps(record)
        if self.bucket:
            self.bucket.blob(f"integration_keys/{key}.json").upload_from_string(raw, content_type="application/json")
        else:
            self.path.mkdir(parents=True, exist_ok=True, mode=0o700)
            tmp = self.path / f".{key}.{uuid.uuid4().hex}.tmp"
            fd = os.open(tmp, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, "w") as f:
                f.write(raw)
            os.replace(tmp, self.path / f"{key}.json")

    def get(self, key):
        if len(key) != 32 or any(c not in "0123456789abcdef" for c in key):
            return None
        if self.bucket:
            from google.api_core.exceptions import NotFound
            try:
                return json.loads(self.bucket.blob(f"integration_keys/{key}.json").download_as_text())
            except NotFound:
                return None
        p = self.path / f"{key}.json"
        return json.loads(p.read_text()) if p.exists() else None

    def records(self):
        if self.bucket:
            return [json.loads(b.download_as_text()) for b in self.bucket.list_blobs(prefix="integration_keys/") if b.name.endswith(".json")]
        return [json.loads(p.read_text()) for p in self.path.glob("*.json")] if self.path.exists() else []

def public(record):
    return {k:v for k,v in record.items() if k != "digest"}

def issue(user, name, grants, expires_at):
    validate_grants(grants)
    if expires_at <= now():
        raise HTTPException(422, "Expiration must be in the future")
    key_id = uuid.uuid4().hex
    token = f"bhk_{key_id}_{secrets.token_urlsafe(32)}"
    record = dict(id=key_id, name=name, grants=grants, expires_at=expires_at.isoformat(), created_at=now().isoformat(), revoked=False,
                  owner_id=user.sub, profile_dir=user.profile_dir, caregiver_id=user.caregiver_id,
                  digest=hashlib.sha256(token.encode()).hexdigest())
    KeyStore().save(record)
    return {**public(record), "secret": token}

def authenticate(token):
    parts = token.split("_", 2)
    record = KeyStore().get(parts[1]) if len(parts) == 3 and parts[0] == "bhk" else None
    if not record or record["revoked"] or datetime.fromisoformat(record["expires_at"]) <= now() or not hmac.compare_digest(record["digest"], hashlib.sha256(token.encode()).hexdigest()):
        raise HTTPException(401, "Invalid or expired API key")
    return record
