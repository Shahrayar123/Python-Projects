import cv2
import dlib

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    i=0

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        #   as the box was small and was barely covering the forehead, I changed x,y to x,y-60
        cv2.rectangle(frame,(x,y-60),(x1,y1),(0,255,0),2)
        i=i+1
        # here i modified the values of (x-10, y-10) so the text shows at the top right corner of the box
        cv2.putText(frame,'face num'+str(i),(x-100,y-70),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
        print(face,i)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()