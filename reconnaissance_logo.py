import pts_communs as ptc
import cv2
import numpy as np
import matplotlib.pyplot as plt

def reco_logo(img1, tab_nom_logo, tab_logo, nb_noms, nb_liens):

	#print(tab_nom_logo)
	#print(tab_logo)
	#print(nb_noms)
	#print(nb_liens)	

	pts_communs_logo = [0]*10
	
	for i in range(nb_noms):
		img2 = cv2.imread(tab_logo[i], cv2.IMREAD_GRAYSCALE) #trainImage

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

		print("Nombre points communs avec le logo " + tab_nom_logo[i] + ": ")
		print(len(good))
		print("\n")

		pts_communs_logo[i] = len(good)
	
	logo_reconnu = 0
	
	for i in range(nb_liens):
		if pts_communs_logo[i] > logo_reconnu:
                       logo_reconnu = pts_communs_logo[i]
		       nom_logo = tab_nom_logo[i]
	
	print("Le logo reconnu est:" + nom_logo)
	
	return nom_logo
