import numpy as np
import cv2

path_to_picture = './pictures/matrix-sunglasses-768x320.jpg'
img = cv2.imread(path_to_picture, cv2.IMREAD_COLOR)
# img = cv2.imread(path_to_picture, cv2.IMREAD_GRAYSCALE)

# get
px = img[55, 55]  # get COLOR of pixel by (x,y) coordinates
print(px)  # [4 4 4] - BGR-color

# set
img[55, 55] = [255, 255, 255]
print(px)  # [255 255 255] - BGR-color

# roi - region of image
roi = img[100:150, 100:150]
print(roi)

img[100:150, 100:150] = [255, 255, 255]

# copy-paste of roi
some_roi = img[0:100, 150:250]
img[150:250, 100:200] = some_roi

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
