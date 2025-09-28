#Imports
from flask import Flask, render_template, redirect, request, flash
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

#My app
app = Flask(__name__)
app.secret_key = "123456"
Scss(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

#MyRoom class
class MyRoom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    occupied = db.Column(db.Integer,default = 0)
    in_use = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"Task {self.id}"
    
#Array for rooms
rooms = []

#Room initialization and append to array
room1 = MyRoom(id=1, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room1)
room2 = MyRoom(id=2, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room2)
room3 = MyRoom(id=3, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room3)
room4 = MyRoom(id=4, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room4)
room5 = MyRoom(id=5, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room5)
room6 = MyRoom(id=6, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room6)
room7 = MyRoom(id=7, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room7)
room8 = MyRoom(id=8, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room8)
room9 = MyRoom(id=9, occupied=0, in_use=datetime.now(timezone.utc))
rooms.append(room9)

#Home page
@app.route("/",methods=["POST","GET"])
def index():
    #Toggle room availability

    if request.method == "POST":
        room_index = int(request.form["room"])
        updateRoom(rooms[room_index])

    return render_template("index.html", rooms=rooms)

#Details page (shows how long the room has been in use)
@app.route("/details/room<int:id>")
def details(id):
    room_data = rooms[id-1]
    elapsed_time = datetime.now(timezone.utc) - rooms[id-1].in_use
    return render_template('details.html', room_data=room_data, elapsed_time=elapsed_time)

#Function to update room availability
def updateRoom(room):
    #If room is occupied, set it to vacant
    if room.occupied:
        room.occupied = 0
    #If room is vacant, set it to occupied and start timer
    else:
        room.occupied = 1
        room.in_use = datetime.now(timezone.utc)
        flash(f"Room {room.id} is now in use!")
    
#Run
if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)