import cv2
import numpy as np
import pyautogui

# Get the size of the screen using pyautogui
SCREEN_SIZE = tuple(pyautogui.size())

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (SCREEN_SIZE))
webcam = cv2.VideoCapture(0)

while True:
    img = pyautogui.screenshot()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    _, frame = webcam.read()
    fr_height, fr_width, _ = frame.shape

    img[0:fr_height, 0: fr_width, :] = frame[0:fr_height, 0: fr_width, :]
    cv2.imshow('frame', img)
    out.write(img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Recording Stopped")
        break

out.release()
cv2.destroyAllWindows()
