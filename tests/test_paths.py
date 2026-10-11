from datetime import datetime
from app.models import JourneyEvent
from app.core.paths import compute_paths, common_next_events

def test_paths(db):
    for u in range(5):
        for i, evt in enumerate(["open", "signup", "pay"]):
            db.add(JourneyEvent(user_id=f"u{u}", event_name=evt, step=i,
                                timestamp=datetime.now()))
    db.commit()
    result = compute_paths(db, top_n=5)
    assert len(result) >= 1
    assert "open -> signup -> pay" in result[0]["path"]

def test_common_next(db):
    for u in range(3):
        db.add(JourneyEvent(user_id=f"u{u}", event_name="open", step=0,
                            timestamp=datetime.now()))
        db.add(JourneyEvent(user_id=f"u{u}", event_name="signup", step=1,
                            timestamp=datetime.now()))
    db.commit()
    result = common_next_events(db, "open", top_n=5)
    assert len(result) >= 1
    assert result[0]["event"] == "signup"
