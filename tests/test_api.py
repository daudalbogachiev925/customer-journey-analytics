def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_add_event(client):
    r = client.post("/api/events", json={
        "user_id": "u1", "event_name": "app_open", "step": 0})
    assert r.status_code == 201

def test_funnel_endpoint(client):
    r = client.post("/api/journeys/funnel",
                     json=["app_open", "signup_start"])
    assert r.status_code == 200
    assert isinstance(r.json(), list)

def test_batch(client):
    r = client.post("/api/events/batch", json=[
        {"user_id": "u1", "event_name": "a", "step": 0},
        {"user_id": "u1", "event_name": "b", "step": 1},
    ])
    assert r.json()["inserted"] == 2
