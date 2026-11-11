"""UI seed JSON and /api/ui/* read endpoints."""
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from main import app
from seed_json_store import SEED_NAMES, clear_cache, seed_dir, ui_app_defaults_dir

client = TestClient(app)


@pytest.fixture(autouse=True)
def _clear_seed_cache(tmp_path):
    from deps import get_profile_repository
    from repositories.json_repository import JsonRepository
    repo = JsonRepository(tmp_path)
    app.dependency_overrides[get_profile_repository] = lambda: repo
    clear_cache()
    yield
    app.dependency_overrides.pop(get_profile_repository, None)
    clear_cache()


@pytest.fixture
def ui_seed_enabled(monkeypatch):
    monkeypatch.setenv("BABYHEALTH_USE_UI_SEED", "1")
    yield
    monkeypatch.delenv("BABYHEALTH_USE_UI_SEED", raising=False)


def test_seed_json_files_exist():
    root = seed_dir()
    for name in SEED_NAMES:
        path = root / f"{name}.json"
        assert path.is_file(), f"Missing {path.relative_to(Path(__file__).resolve().parent.parent)}"


def test_ui_defaults_dir_env_override(monkeypatch, tmp_path):
    monkeypatch.setenv("BABYHEALTH_UI_DEFAULTS_DIR", str(tmp_path))
    assert ui_app_defaults_dir() == tmp_path.resolve()
    assert seed_dir() == tmp_path.resolve()


def test_get_seed_catalogs(ui_seed_enabled):
    r = client.get("/api/ui/seed/catalogs")
    assert r.status_code == 200
    data = r.json()
    assert "logTypes" in data
    assert len(data["logTypes"]) >= 1


def test_get_seed_unknown_404(ui_seed_enabled):
    r = client.get("/api/ui/seed/not_a_real_seed")
    assert r.status_code == 404


def test_ui_bootstrap_contains_core_keys(ui_seed_enabled):
    r = client.get("/api/ui/bootstrap")
    assert r.status_code == 200
    body = r.json()
    for key in (
        "baby",
        "profile_extras",
        "catalogs",
        "content_shell",
        "food_catalog",
        "growth",
        "baby_core",
        "today",
        "timeline_seed",
        "milestones",
        "vaccines",
        "vitamins",
        "health_events",
        "health_detail",
        "caregivers_feed",
        "tracker_logs",
        "tracker_charts",
        "activity_v2",
    ):
        assert key in body, f"missing {key}"
    assert "name" in body["baby"]
    assert "birth_date" in body["baby"]


def test_ui_bootstrap_empty_without_seed_env(monkeypatch):
    monkeypatch.delenv("BABYHEALTH_USE_UI_SEED", raising=False)
    r = client.get("/api/ui/bootstrap")
    assert r.status_code == 200
    body = r.json()
    assert body["catalogs"] == {}
    assert body["food_catalog"] == {"foods": []}
    assert body["today"]["insights"] == []
    assert body["baby"]["id"] == ""
    assert body["baby"]["name"] == ""
    assert len(body["content_shell"]["tabs"]) >= 1


def test_get_seed_disabled_without_env(monkeypatch):
    monkeypatch.delenv("BABYHEALTH_USE_UI_SEED", raising=False)
    r = client.get("/api/ui/seed/catalogs")
    assert r.status_code == 404
    assert "BABYHEALTH_USE_UI_SEED" in r.json()["detail"]
