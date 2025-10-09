from PracticeRooms.practiceRooms import MyRoom, updateRoom
from datetime import datetime, timezone
from unittest.mock import patch

def test_updateRoom():
    startTime = datetime.now(timezone.utc)
    room1 = MyRoom(id=1, occupied=0, in_use=startTime)

    fake_now = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
    with patch("PracticeRooms.practiceRooms.datetime") as mock_datetime:
        mock_datetime.now.return_value = fake_now
        updateRoom(room1)
        assert room1.id == 1
        assert room1.occupied == 1
        assert room1.in_use == fake_now