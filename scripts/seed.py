import random
from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models import JourneyEvent

EVENTS = ["app_open", "signup_start", "signup_complete",
          "onboarding", "first_value", "paywall", "purchase"]

def seed(n_users=500):
    db = SessionLocal()
    try:
        for u in range(n_users):
            path_len = random.randint(2, 7)
            ts = datetime.utcnow() - timedelta(hours=random.randint(1, 500))
            for step in range(path_len):
                db.add(JourneyEvent(
                    user_id=f"u{u}",
                    session_id=f"s{u}_{step}",
                    event_name=random.choice(EVENTS),
                    step=step,
                    timestamp=ts + timedelta(minutes=step * 5),
                ))
        db.commit()
        print(f"Seeded {n_users} users")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
