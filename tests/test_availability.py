# tests/test_availability.py
from app.availability import check_availability

def test_room_available():
    rooms = [{"room": "A", "time": "10:00"}]
    new = {"room": "A", "time": "11:00"}
    assert check_availability(rooms, new) == True

def test_room_unavailable():
    rooms = [{"room": "A", "time": "10:00"}]
    new = {"room": "A", "time": "10:00"}
    assert check_availability(rooms, new) == False
