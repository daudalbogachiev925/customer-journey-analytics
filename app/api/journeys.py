from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas import FunnelStep, PathCount, GraphEdge, NextEvent
from app.core.funnel import compute_funnel
from app.core.paths import compute_paths, common_next_events
from app.core.graph import compute_graph

router = APIRouter()

@router.post("/funnel", response_model=List[FunnelStep])
def funnel(steps: List[str] = Body(...), db: Session = Depends(get_db)):
    return compute_funnel(db, steps)

@router.get("/paths", response_model=List[PathCount])
def paths(top_n: int = 10, db: Session = Depends(get_db)):
    return compute_paths(db, top_n)

@router.get("/next/{current_event}", response_model=List[NextEvent])
def next_events(current_event: str, top_n: int = 10,
                db: Session = Depends(get_db)):
    return common_next_events(db, current_event, top_n)

@router.get("/graph", response_model=List[GraphEdge])
def graph(top_edges: int = 30, db: Session = Depends(get_db)):
    return compute_graph(db, top_edges)
