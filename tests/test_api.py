# tests/test_api.py
import pytest
from app.api import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_reserve_room_success(client):
    response = client.post("/reserve", json={"room": "A", "time": "10:00"})
    assert response.status_code == 201
    assert "message" in response.get_json()

def test_reserve_room_conflict(client):
    client.post("/reserve", json={"room": "B", "time": "15:00"})  # first reservation
    response = client.post("/reserve", json={"room": "B", "time": "15:00"})  # duplicate
    assert response.status_code == 409
    assert "already reserved" in response.get_json()["error"]

def test_reserve_missing_data(client):
    response = client.post("/reserve", json={"room": "C"})
    assert response.status_code == 422
