import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Now we're going to use a form of "brute force" matching. 
We're going to find all features in both images. 
Then we match these features. We then can draw out as many as we want. 
Careful though. If you draw say 500 matches, 
you're going to have a lot of false positives. 
Draw the first few only.
'''

path_to_picture = './pictures/opencv-feature-matching-image.jpg'
path_to_template = './pictures/opencv-feature-matching-template.jpg'

img1 = cv2.imread(path_to_template, 1)
img2 = cv2.imread(path_to_picture, 1)

# the detector we're going to use for the features.
orb = cv2.ORB_create()

# we find the key points and their descriptors with the orb detector.
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Here we create matches of the descriptors,
# then we sort them based on their distances.
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)
plt.imshow(img3)
plt.show()
