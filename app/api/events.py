from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import JourneyEvent
from app.schemas import EventCreate, EventRead

router = APIRouter()

@router.post("", response_model=EventRead, status_code=201)
def add(payload: EventCreate, db: Session = Depends(get_db)):
    e = JourneyEvent(**payload.model_dump())
    db.add(e)
    db.commit()
    db.refresh(e)
    return e

@router.post("/batch", status_code=201)
def add_batch(payloads: List[EventCreate], db: Session = Depends(get_db)):
    for p in payloads:
        db.add(JourneyEvent(**p.model_dump()))
    db.commit()
    return {"inserted": len(payloads)}

@router.get("", response_model=List[EventRead])
def list_events(db: Session = Depends(get_db), limit: int = 5000):
    return db.query(JourneyEvent).limit(limit).all()

@router.delete("", status_code=204)
def delete_all(db: Session = Depends(get_db)):
    db.query(JourneyEvent).delete()
    db.commit()
