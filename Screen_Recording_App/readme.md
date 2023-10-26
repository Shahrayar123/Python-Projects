
## Screen Recording with Webcam Overlay

This Python script allows you to record your screen while overlaying the webcam feed. It uses OpenCV for screen recording and capturing the webcam feed, and PyAutoGUI for taking screenshots.

## Prerequisites

Make sure you have the following libraries installed:

- OpenCV (cv2)
- NumPy (numpy)
- PyAutoGUI (pyautogui)

You can install these libraries using pip:


pip install opencv-python numpy pyautogui


## How to Use

Run the script by executing python screen_recorder.py.

The script will start recording your screen with a webcam overlay. You can adjust the parameters as needed in the script, such as the output file name ('video.avi'), codec ('XVID'), frame rate (20.0), and screen size.

To stop the recording, press 'q'.

The recorded video will be saved as video.avi in the current directory.

## Customization

You can customize the following parameters in the script:

out: Change the output file name and codec.
SCREEN_SIZE: Modify the screen size to match your display.
frame rate: Adjust the frame rate to control the video quality and size.