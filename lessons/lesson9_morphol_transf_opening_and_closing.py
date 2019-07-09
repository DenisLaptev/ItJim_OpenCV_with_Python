import cv2
import numpy as np

'''
opening - удалить белые точки с фона
closing - удалить чёрные точки (неправильные)
'''

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hsv=(Hue,Saturation,Value)

    # hsv=([Hue,Saturation,Value])
    lower_green = np.array([150, 150, 50])
    upper_green = np.array([180, 255, 150])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('result', result)

    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
