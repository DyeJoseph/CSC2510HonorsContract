<h1>Practice Rooms Webapp</h1>

##### Created by Joseph Dye



### Description
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- This webapp was part of a requirement as part of the Honors Program at [Tennessee Tech University](https://www.tntech.edu/). As part of earning my honors credit for the Fall 2025 semester, 
- I contracted my ***Intro to DevOps with Unix (CSC-2510)*** class taught my Mr. Brandon Vandergriff ([vanderbran](https://github.com/vanderbran) on GitHub).
- The goal of this webapp was to create a proof-of-concept of occupancy display and catalogging for the music practice rooms on campus.
- I intended to use GitHub, Python, a VM, Docker, and other related programming techniques to do so.
- This app allows a user to toggle whether a room is occupied or vacant and see how long each room has been occupied.

### Installation (if run locally)
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- Download the application [here](http://madeuplink.com).
- Type `INSERT CODE HERE` into the `command terminal`.
- This application uses a **Docker Image** to simplify the installation process.
- Since this is a webapp, go to http://localhost:5000 to access the running Flask application.

### Webpage
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- However, if you do not want to run this locally, a webpage can be found at 
http://madeuplink.com to access the webapp.
- This website is hosted through **INSERT NAME HERE** and will likely only be up until **INSERT DATE HERE**.

### Tests
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- Several tests have been created and included to test the effectiveness of the database (SQLAlchemy).
- However, I could not figure out how to get the tests to work with [Sweet Alerts](https://sweetalert2.github.io/), which flashes a popup onto the screen when a room is set to be occupied.
- This means that you will need to comment out (using `#`) line `80` in `practiceRooms.py` when running the tests.
- To run the tests, simply type `pytest` into the command line (while in the directory this app is in).
