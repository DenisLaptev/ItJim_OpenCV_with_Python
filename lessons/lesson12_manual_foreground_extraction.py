import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Простой грубый способ удаления фона и выделения переднего плана (foreground extraction)
'''

path_to_big_picture = './pictures/opencv-python-foreground-extraction-tutorial.jpg'
img = cv2.imread(path_to_big_picture)

mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

print(bgdModel)
print(fgdModel)

# The real important part is the rect we define. This is rect = (start_x, start_y, width, height).
# Надо окружить интересующий объект прямоугольником.
rect = (161, 79, 150, 150)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
