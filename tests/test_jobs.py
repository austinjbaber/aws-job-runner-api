from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_and_get_job():
    payload = {
        "satellite_id": "SAT-1",
        "station_id": "GS-1",
        "start": "2025-01-01T00:00:00Z",
        "end":   "2025-01-01T01:00:00Z"
    }
    r = client.post("/jobs", json=payload)
    assert r.status_code == 201  # Changed from 200 to 201 for creation
    job = r.json()
    r2 = client.get(f"/jobs/{job['id']}")
    assert r2.status_code == 200
    assert r2.json()["id"] == job["id"]
