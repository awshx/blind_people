import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

img = cv2.imread('b.jpg')

if img is None:
    print('Could not open the image:')
    exit(0)

height = int(np.size(img, 0)/2)
width = int(np.size(img, 1)/2)
croppedImg = img[0:0+height, width:int(np.size(img, 1))]

gray = cv2.cvtColor(croppedImg,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,150,255)
#lines = cv2.HoughLines(edges,rho=1,theta=np.pi/180,threshold=130)

_, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

num = 0

for cnt in contours:

	perimetre = int(cv2.arcLength(cnt,True))

	if perimetre > 500 and perimetre < 2500:

		approx = cv2.approxPolyDP(cnt,0.01*perimetre,True)
		
		if len(cnt) >= 4 and len(cnt) < 200:

			#cv2.drawContours(croppedImg,[cnt],-1,(0,255,0),2)

			(x, y, w, h) = cv2.boundingRect(cnt)
			newimg = croppedImg[y:y+w, x:x+h]

			#détection couleur

			cv2.imshow("newimg",newimg)

cv2.imshow("croppedImg",croppedImg)
cv2.imshow("edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
