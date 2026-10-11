from collections import Counter
from sqlalchemy.orm import Session
from app.models import JourneyEvent
from app.config import settings

def _group_by_user(db: Session):
    rows = db.query(JourneyEvent).order_by(
        JourneyEvent.user_id, JourneyEvent.step).all()
    by_user = {}
    for r in rows:
        by_user.setdefault(r.user_id, []).append(r.event_name)
    return by_user

def compute_paths(db: Session, top_n: int = 10):
    by_user = _group_by_user(db)
    counter = Counter()
    for events in by_user.values():
        counter[" -> ".join(events[:settings.MAX_PATH_LENGTH])] += 1

    total = sum(counter.values()) or 1
    return [{"path": path, "count": count,
             "share": round(count / total, 4)}
            for path, count in counter.most_common(top_n)]

def common_next_events(db: Session, current_event: str, top_n: int = 10):
    by_user = _group_by_user(db)
    counter = Counter()
    for events in by_user.values():
        for i, e in enumerate(events[:-1]):
            if e == current_event:
                counter[events[i + 1]] += 1

    total = sum(counter.values()) or 1
    return [{"event": e, "count": c, "share": round(c / total, 4)}
            for e, c in counter.most_common(top_n)]
