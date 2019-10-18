import functions as fct
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img2 = cv.imread("logo-pharmacie.png", cv.IMREAD_GRAYSCALE) #trainImage
img1 = cv.imread("rue_logo_banque_postale.jpg", cv.IMREAD_GRAYSCALE) #queryImage

croppedImgLeft = fct.cropImageLeft(img1)

# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

print("nombre matches:")
print(len(good))
print("good")
print(good)

# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


plt.imshow(img3),plt.show()
