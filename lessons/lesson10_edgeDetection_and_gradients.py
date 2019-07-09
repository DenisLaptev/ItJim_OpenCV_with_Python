import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # лапласиан
    # можно использовать, например, для определения контуров, видно более чётко
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    # графиенты (х-,у-компоненты)
    # можно использовать, например, для определения контуров, видно более чётко
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)

    # контуры
    edges = cv2.Canny(frame, 100, 100)

    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
