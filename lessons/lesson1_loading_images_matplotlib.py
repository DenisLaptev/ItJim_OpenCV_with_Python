import cv2
import numpy as np
import matplotlib.pyplot as plt

path_to_picture = './pictures/matrix-sunglasses-768x320.jpg'
img = cv2.imread(path_to_picture, cv2.IMREAD_GRAYSCALE)
# IMREAD_GRAYSCALE = 0
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', 50) #'c'=cian color
plt.show()
