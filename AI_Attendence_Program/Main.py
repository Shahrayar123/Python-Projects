import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

IMAGE_DIR = 'Images'
ATTENDANCE_FILE = 'Attendance.csv'
SCALE_FACTOR = 0.25

def load_images_and_names():
    image_files = os.listdir(IMAGE_DIR)
    images = [cv2.imread(f'{IMAGE_DIR}/{file}') for file in image_files]
    names = [os.path.splitext(file)[0] for file in image_files]
    return images, names

def generate_face_encodings(images):
    return [face_recognition.face_encodings(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))[0] for img in images]

def record_attendance(name):
    with open(ATTENDANCE_FILE, 'r+') as file:
        existing_names = {line.split(',')[0] for line in file.readlines()}
        if name not in existing_names:
            timestamp = datetime.now().strftime('%H:%M:%S,%d/%m/%Y')
            file.write(f'\n{name},{timestamp}')

known_images, known_names = load_images_and_names()
known_encodings = generate_face_encodings(known_images)

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    scaled_frame = cv2.resize(frame, (0, 0), fx=SCALE_FACTOR, fy=SCALE_FACTOR)
    rgb_frame = cv2.cvtColor(scaled_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_encodings, encoding)
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_names[best_match_index].upper()
            top, right, bottom, left = [coord * int(1/SCALE_FACTOR) for coord in location]
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            record_attendance(name)

    cv2.imshow('Video Feed', frame)
    if cv2.waitKey(10) == 13:
        break

video_capture.release()
cv2.destroyAllWindows()
