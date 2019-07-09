import cv2
import numpy as np

path_to_picture1 = './pictures/3D-Matplotlib.png'
path_to_picture2 = './pictures/mainlogo.png'

img1 = cv2.imread(path_to_picture1)
img2 = cv2.imread(path_to_picture2)

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]
# print(channels)#3 channels

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)  # gray version of image img2
ret1, mask1 = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)  # black bg
ret2, mask2 = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY)  # white bg
# Если интенсивность пикселя > 220, то мы заменяем на 255, иначе на 0 (THRESH_BINARY)
# THRESH_BINARY_INV инвертирует черный и белый.


mask_inv = cv2.bitwise_not(mask1)  # white bg

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # маска с белым фоном
img2_fg = cv2.bitwise_and(img2, img2, mask=mask1)  # маска с чёрным фоном

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('mask1', mask1)
cv2.imshow('mask2', mask2)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('result', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
