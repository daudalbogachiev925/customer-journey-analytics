from sqlalchemy.orm import Session
from app.models import JourneyEvent

def compute_funnel(db: Session, steps):
    results = []
    prev_users = None
    for step in steps:
        users = db.query(JourneyEvent.user_id).filter(
            JourneyEvent.event_name == step).distinct().count()
        if prev_users is None:
            conv = 1.0
            drop = 0.0
        else:
            conv = users / prev_users if prev_users else 0.0
            drop = 1 - conv
        results.append({
            "step": step, "users": users,
            "conversion": round(conv, 4),
            "drop_off": round(drop, 4),
        })
        prev_users = users
    return results
