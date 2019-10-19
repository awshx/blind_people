import pts_communs as ptc
import cv2
import numpy as np
import matplotlib.pyplot as plt

def reco_logo(tab_nom_logo, tab_logo):
	img1 = cv2.imread("./logo/mcdo.jpg", cv2.IMREAD_GRAYSCALE) #queryImage

	pts_communs_logo = [0]*10
	
	for i in range(3):
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
	for i in range(3):
		if pts_communs_logo[i] > logo_reconnu:
                       logo_reconnu = pts_communs_logo[i]
		       nom_logo = tab_nom_logo[i]
	
	print("Le logo reconnu est:" + nom_logo)


def logo():
	
	nom_logo1 = "Orange"
	logo1 = "./logo/orange.jpg"
	
	nom_logo2 = "Mcdo"
	logo2 = "./logo/mcdo.jpg"

	nom_logo3 = "Boulanger"
	logo3 = "./logo/boulanger.jpg"

	tab_nom_logo = [nom_logo1, nom_logo2, nom_logo3]
	tab_logo = [logo1, logo2, logo3]

	reco_logo(tab_nom_logo, tab_logo)

logo()
