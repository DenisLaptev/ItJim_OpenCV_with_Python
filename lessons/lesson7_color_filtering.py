import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hsv=(Hue,Saturation,Value)

    # hsv=([Hue,Saturation,Value])
    # розовое полотенце
    lower_green = np.array([150, 150, 50])
    upper_green = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
