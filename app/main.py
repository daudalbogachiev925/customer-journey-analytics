from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api import events, journeys

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Customer Journey Analytics", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(journeys.router, prefix="/api/journeys", tags=["journeys"])

@app.get("/health")
def health():
    return {"status": "ok", "service": "customer-journey-analytics"}
