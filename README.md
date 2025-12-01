<h1>Practice Rooms Webapp</h1>

##### Created by Joseph Dye

### Description
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- This webapp was part of a requirement as part of the Honors Program at [Tennessee Tech University](https://www.tntech.edu/). As part of earning my honors credit for the Fall 2025 semester, I contracted my ***Intro to DevOps with Unix (CSC-2510)*** class taught my Mr. Brandon Vandergriff ([vanderbran](https://github.com/vanderbran) on GitHub).
- The goal of this webapp was to create a proof-of-concept of occupancy display and catalogging for the music practice rooms on campus.
- I intended to use GitHub, Python, a VM, Docker, and other related programming techniques to do so.
- This app allows a user to toggle whether a room is occupied or vacant and see how long each room has been occupied.

### Installation (if run locally)
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- Download the application from GitHub [here](https://github.com/DyeJoseph/CSC2510HonorsContract).
- Type the following lines into the `command terminal` (make sure you are in the directory that `/PracticeRooms` is located in).
    ```
    docker build -t practicerooms-image ./PracticeRooms 
    docker run -p 5002:5002 practicerooms-image
    ```
- This application uses a **Docker Image** to simplify the installation process.
- Since this is a webapp, go to http://localhost:5002 to access the running Flask application.

### Webpage
<hr style="margin-top: 0.1em; margin-bottom: 0.1em;">

- If you do not want to run this locally, you can use Google Cloud Platform's (GCP) Cloud Run to run this.
- Choose **Cloud Run** -> **Create Service**
- Then select clone the repo from GitHub **Cloud Build** -> **Set up with Cloud Build**
- For Build Type, choose **Dockerfile** and set the Source location to *PracticeRooms/Dockerfile*
- Select **Allow Public Access** and set **Maximum number of instances** (1 is fine for testing)
- Then press **Create**
