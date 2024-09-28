import cv2
import numpy as np
import face_recognition
import os

# Get the absolute path of the current file
current_file_path = os.path.abspath(__file__)

# Get the directory path by removing the file name
directory_path = os.path.dirname(current_file_path)

# Print the directory path
print(directory_path)

from datetime import datetime
{
    "configurations": [
        {
            "name": "Mac",
            "includePath": [
                "${workspaceFolder}/**"
            ],
            "defines": [
                "VERSION=1"
            ],
            "macFrameworkPath": [
                "/Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk/System/Library/Frameworks"
            ],
            "compilerPath": "/Users/amakki/Documents/Coding-Design/GitHub/PythonProject/Python-Project/Python-Projects/MaksAI_AttendanceApp/.vscode/c_cpp_properties.json",
            "cStandard": "c17",
            "cppStandard": "c++17",
            "intelliSenseMode": "macos-clang-x64",
            "compilerArgs": [
                "--sysroot <arg>",
                "\"--sysroot\", \"<arg>\""
            ]
        }
    ],
    "version": 4
}

path = 'Images'
Images = []
PersonName = []
mylist = os.listdir(path)
print(mylist)
# for separating the name from their extensions
for cu_img in mylist:
    current_Img = cv2.imread(f'{path}/{cu_img}')
    Images.append(current_Img)
    PersonName.append(os.path.splitext(cu_img)[0])
print(PersonName)

# Add your first image to the 'Images' directory
# Replace 'your_first_image.jpg' with the name of your first image file
first_image = cv2.imread(f'{path}/my_first_image.jpg')
Images.append(first_image)
PersonName.append('Maks First Image')
print(PersonName)


def encodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist


encode_list_Known = encodings(Images)
print("ALL ENCODING FOUND!!!")


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


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

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
            cv2.square(frame, (x1, y1), (x2, y2), (5, 200, 200), 3)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            attendance(name)

    cv2.imshow("camera", frame)
    if cv2.waitKey(10) == 13:
        break
cap.release()
cv2.destroyAllWindows()
def encodings(images):
    """
    This function generates face encodings for a list of images.

    Parameters:
    images (list): A list of images where each image is represented as a numpy array.

    Returns:
    list: A list of face encodings corresponding to the input images.
    """
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
