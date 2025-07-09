from app.api import app

def test_successful_booking():
    client = app.test_client()
    resp = client.post('/reserve', json={"room": "B", "time": "14:00"})
    assert resp.status_code == 201

def test_duplicate_booking():
    client = app.test_client()
    client.post('/reserve', json={"room": "B", "time": "14:00"})
    resp = client.post('/reserve', json={"room": "B", "time": "14:00"})
    assert resp.status_code == 409