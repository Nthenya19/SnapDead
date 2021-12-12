from cv2 import cv2
import cvzone
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    cv2.imshow("Snap Dude", frame)
    if cv2.waitkey(10) == ord("q"):
        break


