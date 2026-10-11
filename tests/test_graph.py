from datetime import datetime
from app.models import JourneyEvent
from app.core.graph import compute_graph

def test_graph(db):
    for u in range(3):
        db.add(JourneyEvent(user_id=f"u{u}", event_name="open", step=0,
                            timestamp=datetime.now()))
        db.add(JourneyEvent(user_id=f"u{u}", event_name="signup", step=1,
                            timestamp=datetime.now()))
    db.commit()
    edges = compute_graph(db, top_edges=10)
    assert any(e["source"] == "open" and e["target"] == "signup"
               for e in edges)
