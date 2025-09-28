from practiceRooms import MyRoom, createRooms, updateRoom
from datetime import datetime, timezone
from unittest.mock import patch

def test_createRooms():
    startTime = datetime.now(timezone.utc)
    rooms = createRooms()

    fake_now = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    with patch("FlaskApp.practiceRooms.datetime") as mock_datetime:
        mock_datetime.now.return_value = fake_now
        
        for i in range (0, 8):
            updateRoom(rooms[i])
            assert rooms[i].id == i
            assert rooms[i].occupied == 1
            assert rooms[i].in_use == fake_now

        for i in range (0, 8, -1):
            updateRoom(rooms[i])
            assert rooms[i].id == i
            assert rooms[i].occupied == 0
            assert rooms[i].in_use == fake_now