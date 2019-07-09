import cv2
import numpy as np

'''
Нахождение углов на рисунке
'''

path_to_picture = './pictures/opencv-corner-detection-sample.jpg'
img = cv2.imread(path_to_picture)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

print('gray')
print(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

print('corners')
print(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
