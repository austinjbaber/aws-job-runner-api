from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

FAKE_DB = {}  # in-memory for now

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/jobs")
def create_job():
    job_id = str(uuid4())
    FAKE_DB[job_id] = {"id": job_id, "status": "queued"}
    return FAKE_DB[job_id]

@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    job = FAKE_DB.get(job_id)
    if not job:
        return {"error": "not found"}
    return job
