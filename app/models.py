from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class JobStatus(str, Enum):
    queued = "queued"
    running = "running"
    done = "done"

class JobCreate(BaseModel):
    satellite_id: str
    station_id: str
    start: datetime
    end: datetime

class Job(BaseModel):
    id: str
    status: JobStatus
    satellite_id: str
    station_id: str
    start: datetime
    end: datetime
    created_at: datetime
