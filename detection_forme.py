import numpy as np
import pts_communs as pc
import cv2
from matplotlib import pyplot as plt
import math

def image():
	
	image = './Images_rue/72330137_399179944080045_6899828685730217984_n.jpg'
	return image

def detect_shape():

	img = cv2.imread(image())

	if img is None:
		print('Could not open the image:')
    		exit(0)

	croppedImg = pc.cropImageRight(img)

	gray = cv2.cvtColor(croppedImg,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,150,255)
	#lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

	_, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	num = 0
	tab_formes = []

	for cnt in contours:

		perimetre = int(cv2.arcLength(cnt,True))

		if perimetre > 500 and perimetre < 2500:

			approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
		
			if len(cnt) >= 4 and len(cnt) < 250:

				#cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

				(x, y, w, h) = cv2.boundingRect(cnt)
				newimg = croppedImg[y:y+w, x:x+h]
				heightCropped = int(np.size(newimg, 0))
				widthCropped = int(np.size(newimg, 1))
			
							
				if (heightCropped/widthCropped) < 1.2 and (heightCropped/widthCropped) >= 0.8:

					forme = './Images_detection_formes/forme' + str(num) + '.jpg'	
					cv2.imwrite(forme , newimg)
					tab_formes.append(forme)
                        		num += 1

	return tab_formes


def coordonnees_centrale_logo():

	img = cv2.imread(image())

	if img is None:
		print('Could not open the image:')
    		exit(0)

	croppedImg = pc.cropImageRight(img)
	yInitiale = 0
	xInitiale = int(np.size(img, 1)/3)*2

	gray = cv2.cvtColor(croppedImg,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,150,255)
	#lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

	_, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	num = 0
	tab_formes = []

	for cnt in contours:

		perimetre = int(cv2.arcLength(cnt,True))

		if perimetre > 500 and perimetre < 2500:

			approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
		
			if len(cnt) >= 4 and len(cnt) < 250:

				#cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

				(x, y, w, h) = cv2.boundingRect(cnt)
				newimg = croppedImg[y:y+w, x:x+h]
				heightCropped = int(np.size(newimg, 0))
				widthCropped = int(np.size(newimg, 1))
			
							
				if (heightCropped/widthCropped) < 1.2 and (heightCropped/widthCropped) >= 0.8:
					coordo_centrale = []
					coordo_X = xInitiale+x+(widthCropped/2)
					coordo_Y = yInitiale+y+(heightCropped/2)
					cv2.circle(img, (coordo_X, coordo_Y), 7, (0,0,255), -1)
					cv2.imwrite('./Images_detection_formes/coordoCentrale.jpg', img)
					coordo_centrale.append(coordo_X)
					coordo_centrale.append(coordo_Y)

	return coordo_centrale
