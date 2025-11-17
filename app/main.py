from fastapi import FastAPI, HTTPException
from uuid import uuid4
from datetime import datetime

from .models import JobCreate, Job, JobStatus

app = FastAPI()

FAKE_DB = {}  # in-memory for now

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/jobs", response_model=Job, status_code=201)
def create_job(payload: JobCreate):
    job_id = str(uuid4())
    job = Job(
        id=job_id,
        status=JobStatus.queued,
        created_at=datetime.utcnow(),
        **payload.model_dump()
    )
    FAKE_DB[job_id] = job
    return job

@app.get("/jobs/{job_id}", response_model=Job)
def get_job(job_id: str):
    job = FAKE_DB.get(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@app.get("/jobs", response_model=list[Job])
def list_jobs():
    return list(FAKE_DB.values())