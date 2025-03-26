
## Face Recognition Attendance System

This is a Python script that uses the OpenCV and face_recognition libraries to create a simple face recognition attendance system. It captures images from a camera, recognizes faces, and logs attendance in a CSV file.


## Prerequisites

Before running the code, you need to install the required Python libraries. You can install them using pip:

- pip install -r requirements.txt


## Usage

- Create a folder named 'Images' in the same directory as this script.
- Add images of the individuals you want to recognize in the 'Images' folder. 
- The images should have only one face per image.
- Run the script.


## How it works

- The script loads the known face encodings from the 'Images' folder.
- It captures video from the default camera.
- For each frame of video, it detects faces and encodes them.
- It compares the encodings of detected faces with the known face encodings.
- If a match is found, it records the name of the recognized person and the timestamp in the 'Attendance.csv' file.
- The video stream is displayed with rectangles around the recognized faces and their names.

## File Structure

-- Images: Store images of individuals you want to recognize.
-- Attendance.csv: Stores attendance records with name, time, and date.
