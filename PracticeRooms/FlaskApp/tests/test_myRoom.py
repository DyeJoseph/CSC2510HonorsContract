from FlaskApp.practiceRooms import MyRoom
from datetime import datetime, timezone

def test_MyRoom():
    startTime = datetime.now(timezone.utc)
    room1 = MyRoom(id=1, occupied=0, in_use=startTime)
    assert room1.id == 1
    assert room1.occupied == 0
    assert room1.in_use == startTime

