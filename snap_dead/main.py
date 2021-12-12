from cv2 import cv2
import cvzone
cap = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    _, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Snap Dude", frame)
    if cv2.waitkey(10) == ord("q"):
        break


