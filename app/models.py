from sqlalchemy import Column, Integer, String, DateTime, Index
from sqlalchemy.sql import func
from app.database import Base

class JourneyEvent(Base):
    __tablename__ = "journey_events"
    id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True, nullable=False)
    session_id = Column(String, index=True)
    event_name = Column(String, index=True, nullable=False)
    step = Column(Integer, default=0)
    properties = Column(String)
    timestamp = Column(DateTime, server_default=func.now(), index=True)

    __table_args__ = (
        Index("ix_user_step", "user_id", "step"),
        Index("ix_event_time", "event_name", "timestamp"),
    )
