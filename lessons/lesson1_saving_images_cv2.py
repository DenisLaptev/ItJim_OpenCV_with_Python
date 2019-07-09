import cv2
import numpy as np
import matplotlib.pyplot as plt

path_to_picture = './pictures/matrix-sunglasses-768x320.jpg'
img = cv2.imread(path_to_picture, cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./pictures/matrix_gray.png', img)
