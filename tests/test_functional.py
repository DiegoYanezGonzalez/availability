from app.api import app

def test_reserve_room_success():
    client = app.test_client()
    response = client.post("/reserve", data={"room": "A", "time": "10:00"})
    assert response.status_code == 201

def test_reserve_room_conflict():
    client = app.test_client()
    client.post("/reserve", json={"room": "B", "time": "15:00"})  # First
    response = client.post("/reserve", data={"room": "B", "time": "15:00"})  # Conflict
    assert response.status_code == 409
    assert "not available" in response.get_json()["message"]

def test_reserve_missing_data():
    client = app.test_client()
    response = client.post("/reserve", data={"room": "C"})
    assert response.status_code == 422
