from FlaskApp.practiceRooms import MyRoom, updateRoom, app
from datetime import datetime, timezone
from unittest.mock import patch
from flask import Flask, render_template, redirect, request, flash

def test_updateRoom():
    with app.app_context():
        startTime = datetime.now(timezone.utc)
        room1 = MyRoom(id=1, occupied=0, in_use=startTime)

        fake_now = datetime(2025, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        with patch("FlaskApp.practiceRooms.datetime") as mock_datetime:
            mock_datetime.now.return_value = fake_now
            updateRoom(room1)
            assert room1.id == 1
            assert room1.occupied == 1
            assert room1.in_use == fake_now