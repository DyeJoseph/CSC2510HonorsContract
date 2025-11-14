import eventlet
eventlet.monkey_patch()

#Imports
from flask import Flask, render_template, redirect, request, flash
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from flask_socketio import SocketIO, emit
import os

#My app
app = Flask(__name__)
socketio = SocketIO(app)
app.secret_key = "123456"
Scss(app)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://username:password@localhost:5432/dbname"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
db = SQLAlchemy(app)

#MyRoom class
class MyRoom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    occupied = db.Column(db.Integer,default = 0)
    in_use = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return f"Task {self.id}"
    
def createRooms():
    if MyRoom.query.count() == 0:
        for i in range(1, 10):
            room = MyRoom(id=i, occupied=0, in_use=datetime.now())
            db.session.add(room)
        db.session.commit()

#Home page
@app.route("/",methods=["POST","GET"])
def index():
    #Toggle room availability

    if request.method == "POST":
        room_index = int(request.form["room"]) + 1
        with app.app_context():
            room = db.session.get(MyRoom, room_index)
            updateRoom(room)
    rooms = MyRoom.query.order_by(MyRoom.id).all()
    return render_template("index.html", rooms=rooms)

#Details page (shows how long the room has been in use)
@app.route("/details/room<int:id>")
def details(id):
    rooms = MyRoom.query.order_by(MyRoom.id).all()
    room_data = rooms[id-1]
    elapsed_time = datetime.now() - rooms[id-1].in_use
    return render_template('details.html', room_data=room_data, elapsed_time=elapsed_time)

#Function to update room availability
def updateRoom(room):
    #If room is occupied, set it to vacant
    if room.occupied:
        room.occupied = 0
    #If room is vacant, set it to occupied and start timer
    else:
        room.occupied = 1
        room.in_use = datetime.now()
        #Comment out the line below this if running tests
        # flash(f"Room {room.id} is now in use!")
    db.session.commit()
    socketio.emit('refresh')
    
#Run
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        createRooms()
    socketio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)
    # socketio.run(app, host="0.0.0.0", port=8080)
    # app.run(host="0.0.0.0", port=8080)
