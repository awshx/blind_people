import numpy as np
import pts_communs as pc
import cv2
from matplotlib import pyplot as plt
import math

def detect_shape():

	img = cv2.imread('./Images_rue/71810630_2435283783192683_6445654989602816_n.jpg')

	if img is None:
		print('Could not open the image:')
    		exit(0)

	croppedImg = pc.cropImageLeft(img)

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
                        		#cv2.imshow("forme", newimg)
					#cv2.imshow("croppedImg", croppedImg)
					#cv2.waitKey(5000)
					cv2.imwrite(forme , newimg)
					tab_formes.append(forme)
                        		num += 1

	#cv2.destroyAllWindows()
	return tab_formes
