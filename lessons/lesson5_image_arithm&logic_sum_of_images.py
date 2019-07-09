import cv2
import numpy as np

path_to_picture1 = './pictures/3D-Matplotlib.png'
path_to_picture2 = './pictures/mainsvmimage.png'

img1 = cv2.imread(path_to_picture1)
img2 = cv2.imread(path_to_picture2)

# совмещение двух рисунков на одном.
plus = img1 + img2

cv2.imshow('img1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('img2', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('plus', plus)
cv2.waitKey(0)
cv2.destroyAllWindows()

# В результирующем рисунке значение каждого пикселя=
# =сумма значений соответствующих пикселей двух рисунков
add2 = cv2.add(img1, img2)
# (155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255)


cv2.imshow('add2', add2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# В результирующем рисунке значение каждого пикселя=
# =сумма значений соответствующих пикселей двух рисунков
add_weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('add_weighted', add_weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
