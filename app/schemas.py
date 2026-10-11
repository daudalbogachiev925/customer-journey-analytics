from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class EventCreate(BaseModel):
    user_id: str
    session_id: Optional[str] = None
    event_name: str
    step: int = 0
    properties: Optional[str] = None

class EventRead(EventCreate):
    id: int
    class Config:
        from_attributes = True

class FunnelStep(BaseModel):
    step: str
    users: int
    conversion: float
    drop_off: float

class PathCount(BaseModel):
    path: str
    count: int
    share: float

class GraphEdge(BaseModel):
    source: str
    target: str
    count: int

class NextEvent(BaseModel):
    event: str
    count: int
    share: float
