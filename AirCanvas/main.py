import numpy as np
import cv2
from collections import deque

def setValues():
    pass

cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180, setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255, setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180, setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255, setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255, setValues)

bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]

blue_index = green_index = red_index = yellow_index = 0
kernel = np.ones((5, 5), np.uint8)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0

paintWindow = np.zeros((471, 636, 3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40, 1), (140, 65), (0, 0, 0), 2)
for i, color in enumerate(colors):
    paintWindow = cv2.rectangle(paintWindow, (160 + 115 * i, 1), (255 + 115 * i, 65), color, -1)

cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
for i, text in enumerate(["BLUE", "GREEN", "RED", "YELLOW"]):
    cv2.putText(paintWindow, text, (185 + 115 * i, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue, u_saturation, u_value])
    Lower_hsv = np.array([l_hue, l_saturation, l_value])

    frame = cv2.rectangle(frame, (40, 1), (140, 65), (122, 122, 122), -1)
    for i, color in enumerate(colors):
        frame = cv2.rectangle(frame, (160 + 115 * i, 1), (255 + 115 * i, 65), color, -1)

    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    for i, text in enumerate(["BLUE", "GREEN", "RED", "YELLOW"]):
        cv2.putText(frame, text, (185 + 115 * i, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)

    cnts, _ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if center[1] <= 65:
            if 40 <= center[0] <= 140:
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                blue_index = green_index = red_index = yellow_index = 0
                paintWindow[67:, :, :] = 255
            elif 160 <= center[0] <= 255:
                colorIndex = 0
            elif 275 <= center[0] <= 370:
                colorIndex = 1
            elif 390 <= center[0] <= 485:
                colorIndex = 2
            elif 505 <= center[0] <= 600:
                colorIndex = 3
        else:
            [bpoints, gpoints, rpoints, ypoints][colorIndex][[blue_index, green_index, red_index, yellow_index][colorIndex]].appendleft(center)
    else:
        for points in [bpoints, gpoints, rpoints, ypoints]:
            points.append(deque(maxlen=512))
        blue_index += 1
        green_index += 1
        red_index += 1
        yellow_index += 1

    for i, color in enumerate(colors):
        for j in range(len([bpoints, gpoints, rpoints, ypoints][i])):
            for k in range(1, len([bpoints, gpoints, rpoints, ypoints][i][j])):
                if [bpoints, gpoints, rpoints, ypoints][i][j][k - 1] and [bpoints, gpoints, rpoints, ypoints][i][j][k]:
                    cv2.line(frame, [bpoints, gpoints, rpoints, ypoints][i][j][k - 1], [bpoints, gpoints, rpoints, ypoints][i][j][k], color, 2)
                    cv2.line(paintWindow, [bpoints, gpoints, rpoints, ypoints][i][j][k - 1], [bpoints, gpoints, rpoints, ypoints][i][j][k], color, 2)

    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(4) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
