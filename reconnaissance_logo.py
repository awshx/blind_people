import pts_communs as ptc
import cv2
import numpy as np
import matplotlib.pyplot as plt

def reco_logo():

	img1 = cv2.imread("./Images_rue/72330137_399179944080045_6899828685730217984_n.jpg", cv2.IMREAD_GRAYSCALE) #queryImage
	img2 = cv2.imread("./logo/lcl.jpg", cv2.IMREAD_GRAYSCALE) #trainImage

	croppedImgLeft = ptc.cropImageLeft(img1)

	# Initiate SIFT detector
	sift = cv2.xfeatures2d.SIFT_create()

	# find the keypoints and descriptors with SIFT
	kp1, des1 = sift.detectAndCompute(img1,None)
	kp2, des2 = sift.detectAndCompute(img2,None)

	# BFMatcher with default params
	bf = cv2.BFMatcher()
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
	img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


	plt.imshow(img3),plt.show()


reco_logo()
