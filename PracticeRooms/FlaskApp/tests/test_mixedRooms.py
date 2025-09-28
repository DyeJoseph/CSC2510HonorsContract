from FlaskApp.practiceRooms import MyRoom, createRooms, updateRoom
from datetime import datetime, timezone
from unittest.mock import patch

def test_mixedRooms():
    startTime = datetime.now(timezone.utc)
    rooms = []

    room1 = MyRoom(id=1, occupied=1, in_use=startTime)
    rooms.append(room1)
    room2 = MyRoom(id=2, occupied=1, in_use=startTime)
    rooms.append(room2)
    room3 = MyRoom(id=3, occupied=1, in_use=startTime)
    rooms.append(room3)
    room4 = MyRoom(id=4, occupied=0, in_use=startTime)
    rooms.append(room4)
    room5 = MyRoom(id=5, occupied=0, in_use=startTime)
    rooms.append(room5)

    for i in range(0,3):
        assert rooms[i].id == i+1
        assert rooms[i].occupied == 1
        assert rooms[i].in_use == startTime

    for i in range(3,5):
        assert rooms[i].id == i+1
        assert rooms[i].occupied == 0
        assert rooms[i].in_use == startTime

    fake_now = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    with patch("FlaskApp.practiceRooms.datetime") as mock_datetime:
        mock_datetime.now.return_value = fake_now
        
        for i in rooms:
            updateRoom(i)
        
        for i in range(0,3):
            assert rooms[i].id == i+1
            assert rooms[i].occupied == 0
            assert rooms[i].in_use == startTime

        for i in range(3,5):
            assert rooms[i].id == i+1
            assert rooms[i].occupied == 1
            assert rooms[i].in_use == fake_now


