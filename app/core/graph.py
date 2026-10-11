from collections import Counter
from sqlalchemy.orm import Session
from app.models import JourneyEvent

def compute_graph(db: Session, top_edges: int = 30):
    rows = db.query(JourneyEvent).order_by(
        JourneyEvent.user_id, JourneyEvent.step).all()
    by_user = {}
    for r in rows:
        by_user.setdefault(r.user_id, []).append(r.event_name)

    counter = Counter()
    for events in by_user.values():
        for a, b in zip(events, events[1:]):
            counter[(a, b)] += 1

    return [{"source": a, "target": b, "count": c}
            for (a, b), c in counter.most_common(top_edges)]
