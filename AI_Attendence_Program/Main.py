import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

# Path to the images
path = 'Images'

# Initialize lists for images and names
Images = []
PersonName = []
mylist = os.listdir(path)
print(mylist)

# Load images and extract names
for cu_img in mylist:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    Images.append(current_Img)
    PersonName.append(os.path.splitext(cu_img)[0])
print(PersonName)

# Function to encode faces
def encodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

# Get encodings of all known faces
encode_list_Known = encodings(Images)
print("ALL ENCODING FOUND!!!")

# Function to record attendance
def attendance(name):
    with open('Attendence.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tStr},{dStr}')

# Access the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is accessible
if not cap.isOpened():
    print("Error: Camera not accessible")
    exit()

# Loop to capture frames and detect faces
while True:
    ret, frame = cap.read()
    
    # If frame is read correctly, ret will be True
    if not ret:
        print("Failed to grab frame")
        break

    # Resize and convert frame for faster processing
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    # Get face locations and encodings in the current frame
    faces_currentframe = face_recognition.face_locations(faces)
    encode_currentframe = face_recognition.face_encodings(faces, faces_currentframe)

    for encodeFace, faceLoc in zip(encode_currentframe, faces_currentframe):
        matches = face_recognition.compare_faces(encode_list_Known, encodeFace)
        faceDistance = face_recognition.face_distance(encode_list_Known, encodeFace)

        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = PersonName[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            #y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            attendance(name)

    # Display the frame with the rectangle and name
    cv2.imshow("camera", frame)

    # Break the loop if the Enter key is pressed
    if cv2.waitKey(10) == 13:  # ASCII code for Enter key
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
