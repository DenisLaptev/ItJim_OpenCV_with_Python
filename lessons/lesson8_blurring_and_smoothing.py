import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # hsv=(Hue,Saturation,Value)

    # hsv=([Hue,Saturation,Value])
    # розовое полотенце
    lower_green = np.array([0, 0, 0])
    upper_green = np.array([255, 255, 250])

    mask = cv2.inRange(hsv, lower_green, upper_green)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # 1
    kernel = np.ones((15, 15), np.float32) / 225
    print(kernel)

    # 2
    smoothed = cv2.filter2D(result, -1, kernel)

    # 3
    blur = cv2.GaussianBlur(result, (15, 15), 0)

    # 4
    median = cv2.medianBlur(result, 15)

    # 5
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('smoothed', smoothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
