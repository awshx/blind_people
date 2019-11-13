import numpy as np
import pts_communs as pc
import cv2
from matplotlib import pyplot as plt
import math

def image():
	
	image = './Images_rue/Image7.jpg'
	return image

def detect_shape():

	img = cv2.imread(image())
	num = 0
	tab_formes = [0]*1

	if img is None:
		print('Could not open the image:')
    		exit(0)

	croppedImgRight = pc.cropImageRight(img)
	croppedImgLeft = pc.cropImageLeft(img)

	grayRight = cv2.cvtColor(croppedImgRight,cv2.COLOR_BGR2GRAY)
	edgesRight = cv2.Canny(grayRight,150,255)
	#lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

	_, contoursRight, _ = cv2.findContours(edgesRight, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cntRight in contoursRight:

		perimetreRight = int(cv2.arcLength(cntRight,True))

		if perimetreRight > 500 and perimetreRight < 2500:

			approxRight = cv2.approxPolyDP(cntRight,0.01*perimetreRight,True)
		
			if len(cntRight) >= 4 and len(cntRight) < 250:

				#cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

				(x, y, w, h) = cv2.boundingRect(cntRight)
				newimgRight = croppedImgRight[y:y+w, x:x+h]
				heightCroppedRight = int(np.size(newimgRight, 0))
				widthCroppedRight = int(np.size(newimgRight, 1))
			
							
				if (heightCroppedRight/widthCroppedRight) < 1.2 and (heightCroppedRight/widthCroppedRight) >= 0.8:

					forme = './Images_detection_formes/forme' + str(num) + '.jpg'	
					cv2.imwrite(forme , newimgRight)
					#tab_formes.append(forme)
					tab_formes[0] = forme
                        		num += 1
	
	grayLeft = cv2.cvtColor(croppedImgLeft,cv2.COLOR_BGR2GRAY)
        edgesLeft = cv2.Canny(grayLeft,150,255)
        #lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

        _, contoursLeft, _ = cv2.findContours(edgesLeft, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cntLeft in contoursLeft:

                perimetreLeft = int(cv2.arcLength(cntLeft,True))

                if perimetreLeft > 500 and perimetreLeft < 2500:

                        approxLeft = cv2.approxPolyDP(cntLeft,0.01*perimetreLeft,True)

                        if len(cntLeft) >= 4 and len(cntLeft) < 250:

                                #cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

                                (x, y, w, h) = cv2.boundingRect(cntLeft)
                                newimgLeft = croppedImgLeft[y:y+w, x:x+h]
                                heightCroppedLeft = int(np.size(newimgLeft, 0))
                                widthCroppedLeft = int(np.size(newimgLeft, 1))

				if (heightCroppedLeft/widthCroppedLeft) < 1.2 and (heightCroppedLeft/widthCroppedLeft) >= 0.8:

                                        forme = './Images_detection_formes/forme' + str(num) + '.jpg'
                                        cv2.imwrite(forme , newimgLeft)
                                        #tab_formes.append(forme)
                                        tab_formes[0] = forme
					num += 1

	return tab_formes


def coordonnees_centrale_logo():

	img = cv2.imread(image())

	if img is None:
		print('Could not open the image:')
    		exit(0)

	croppedImgLeft = pc.cropImageLeft(img)
	croppedImgRight = pc.cropImageRight(img)	

	yInitiale = 0
	xInitiale = int(np.size(img, 1)/3)*2

	grayLeft = cv2.cvtColor(croppedImgLeft,cv2.COLOR_BGR2GRAY)
	edgesLeft = cv2.Canny(grayLeft,150,255)
	#lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

	_, contoursLeft, _ = cv2.findContours(edgesLeft, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	for cntLeft in contoursLeft:

		perimetreLeft = int(cv2.arcLength(cntLeft,True))

		if perimetreLeft > 500 and perimetreLeft < 2500:

			approxLeft = cv2.approxPolyDP(cntLeft,0.01*perimetreLeft,True)
		
			if len(cntLeft) >= 4 and len(cntLeft) < 250:

				#cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

				(x, y, w, h) = cv2.boundingRect(cntLeft)
				newimgLeft = croppedImgLeft[y:y+w, x:x+h]
				heightCroppedLeft = int(np.size(newimgLeft, 0))
				widthCroppedLeft = int(np.size(newimgLeft, 1))
			
							
				if (heightCroppedLeft/widthCroppedLeft) < 1.2 and (heightCroppedLeft/widthCroppedLeft) >= 0.8:
					coordo_centrale = []
					coordo_X = xInitiale-(x+(widthCroppedLeft/2)+400)
					coordo_Y = yInitiale+y+(heightCroppedLeft/2)
					cv2.circle(img, (coordo_X, coordo_Y), 7, (0,0,255), -1)
					cv2.imwrite('./Images_detection_formes/coordoCentrale.jpg', img)
					coordo_centrale.append(coordo_X)
					coordo_centrale.append(coordo_Y)
	
	grayRight = cv2.cvtColor(croppedImgRight,cv2.COLOR_BGR2GRAY)
        edgesRight = cv2.Canny(grayRight,150,255)
        #lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

        _, contoursRight, _ = cv2.findContours(edgesRight, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cntRight in contoursRight:

                perimetreRight = int(cv2.arcLength(cntRight,True))

                if perimetreRight > 500 and perimetreRight < 2500:

                        approxRight = cv2.approxPolyDP(cntRight,0.01*perimetreRight,True)

                        if len(cntRight) >= 4 and len(cntRight) < 250:

                                #cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

                                (x, y, w, h) = cv2.boundingRect(cntRight)
                                newimgRight = croppedImgRight[y:y+w, x:x+h]
                                heightCroppedRight = int(np.size(newimgRight, 0))
                                widthCroppedRight = int(np.size(newimgRight, 1))

				if (heightCroppedRight/widthCroppedRight) < 1.2 and (heightCroppedRight/widthCroppedRight) >= 0.8:
                                        coordo_centrale = []
                                        coordo_X = xInitiale+x+(widthCroppedRight/2)
                                        coordo_Y = yInitiale+y+(heightCroppedRight/2)
                                        cv2.circle(img, (coordo_X, coordo_Y), 7, (0,0,255), -1)
                                        cv2.imwrite('./Images_detection_formes/coordoCentrale.jpg', img)
                                        coordo_centrale.append(coordo_X)
                                        coordo_centrale.append(coordo_Y)

				
	return coordo_centrale
