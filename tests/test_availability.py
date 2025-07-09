from app.availability import verificar_disponibilidad

def test_room_available():
    rooms = [
        {"room": "A", "time": "10:00"},
        {"room": "A", "time": "11:00"}
    ]
    new = {"room": "A", "time": "12:00"}
    assert verificar_disponibilidad(rooms, new) == True

def test_room_unavailable():
    rooms = [
        {"room": "A", "time": "10:00"},
        {"room": "A", "time": "11:00"}
    ]
    new = {"room": "A", "time": "11:00"}
    assert verificar_disponibilidad(rooms, new) == False
