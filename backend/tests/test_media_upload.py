"""Profile images under DATA_DIR/images/."""
import io
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

import config

# 1x1 transparent PNG
MIN_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d49484452000000010000000108060000001f15c489"
    "0000000a49444154789c630001000005000167d8d5c80000000049454e44ae426082"
)


@pytest.fixture
def media_client(monkeypatch, tmp_path: Path) -> TestClient:
    monkeypatch.setattr(config.settings, "data_dir", tmp_path)
    from main import app

    from deps import get_current_user
    from models.auth import TokenPayload
    monkeypatch.setattr(config.settings, "storage_type", "json")
    app.dependency_overrides[get_current_user] = lambda: TokenPayload(sub="test", username="test", profile_dir="family", caregiver_id="test")
    yield TestClient(app)
    app.dependency_overrides.pop(get_current_user, None)


def test_upload_and_get_image(media_client: TestClient, tmp_path: Path):
    r = media_client.post(
        "/api/media/upload",
        files={"file": ("test.png", io.BytesIO(MIN_PNG), "image/png")},
    )
    assert r.status_code == 200
    data = r.json()
    assert "url" in data
    assert data["url"].startswith("/api/media/")
    name = data["url"].split("/")[-1]
    img_dir = tmp_path / "family" / "images"
    assert (img_dir / name).is_file()

    g = media_client.get(f"/api/media/{name}")
    assert g.status_code == 200
    assert g.content == MIN_PNG


def test_upload_rejects_large_file(media_client: TestClient, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("routers.media.MAX_FILE_BYTES", 100)
    big = b"x" * 101
    r = media_client.post(
        "/api/media/upload",
        files={"file": ("huge.png", io.BytesIO(big), "image/png")},
    )
    assert r.status_code == 413


def test_upload_rejects_bad_type(media_client: TestClient):
    r = media_client.post(
        "/api/media/upload",
        files={"file": ("x.txt", io.BytesIO(b"hello"), "text/plain")},
    )
    assert r.status_code == 400


def test_get_unknown_404(media_client: TestClient):
    assert media_client.get("/api/media/not-a-real-name.png").status_code == 404
