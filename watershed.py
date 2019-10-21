import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread('b.jpg')

if img is None:
    print('Could not open the image:')
    exit(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

height = int(np.size(img, 0)/2)
width = int(np.size(img, 1)/2)
croppedImg = thresh[0:0+height, width:int(np.size(img, 1))]


_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


for cnt in contours:

	perimetre = int(cv2.arcLength(cnt,True))
	
	if perimetre > 500 and perimetre < 1000:
		
		approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
		cv2.drawContours(img,[cnt],-1,(0,255,0),2)
		lines = cv2.HoughLines(croppedImg,rho=1,theta=np.pi/180,threshold=130)

		'''
		if len(cnt) >= 4 and len(cnt) < 50:			
			(x, y, w, h) = cv2.boundingRect(approx)
			ratio = w / float(h)
			
			if ratio >= 0.95 and ratio <= 1.05:
				shape = "carre"
				print(shape)
			else:
				shape = "rectangle"
				print(shape)
		'''
	#cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	
cv2.imshow("image", img)
cv2.imshow("gray",gray)
cv2.imshow("Threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()