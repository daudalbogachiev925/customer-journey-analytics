from datetime import datetime
from app.models import JourneyEvent
from app.core.funnel import compute_funnel

def test_funnel_empty(db):
    result = compute_funnel(db, ["a", "b"])
    assert all(s["users"] == 0 for s in result)

def test_funnel_basic(db):
    for u in range(10):
        db.add(JourneyEvent(user_id=f"u{u}", event_name="app_open",
                            step=0, timestamp=datetime.now()))
    for u in range(5):
        db.add(JourneyEvent(user_id=f"u{u}", event_name="signup",
                            step=1, timestamp=datetime.now()))
    db.commit()
    result = compute_funnel(db, ["app_open", "signup"])
    assert result[0]["users"] == 10
    assert result[1]["users"] == 5
    assert result[1]["conversion"] == 0.5
    assert result[1]["drop_off"] == 0.5
