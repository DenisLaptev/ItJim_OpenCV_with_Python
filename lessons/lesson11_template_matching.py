import cv2
import numpy as np

path_to_big_picture = './pictures/opencv-template-matching-python-tutorial.jpg'
path_to_small_picture = './pictures/opencv-template-for-matching.jpg'

img_bgr = cv2.imread(path_to_big_picture)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread(path_to_small_picture, 0)
w, h = template.shape[::-1]

# проходим по большой картинке и находим соответствие с маленькой,
# когда находим, сохраняем координаты в np.array.
result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.7
loc = np.where(result >= threshold)

# помечаем на исходной картинке совпадения жёлтыми прямоугольниками.
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

cv2.imshow('img_bgr', img_bgr)
cv2.imshow('detected', img_bgr)
cv2.imshow('img_gray', img_gray)
cv2.imshow('template', template)

cv2.waitKey(0)
cv2.destroyAllWindows()
