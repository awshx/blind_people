import numpy as np
import cv2
import matplotlib.pyplot as plt

def choixImage():
	image = cv2.imread("../Images_rue/Image9.jpg")
	return image

def imageCenter():

	image = choixImage()

	heightCropped = int(np.size(image, 0)/3)
	widthCropped = int(np.size(image, 1)/3)

	croppedImg = image[heightCropped+110:heightCropped*2+110,widthCropped:widthCropped*2]
	#cv2.imwrite("./test.jpg", croppedImg)

	return croppedImg

def detect_road():

	croppedImg = imageCenter()
	image_finale = choixImage()
        hC = int(np.size(image_finale, 0)/3)
        wC = int(np.size(image_finale, 1)/3)	

	#gray = cv2.cvtColor(croppedImg, cv2.COLOR_BGR2GRAY)
	#gray = cv2.equalizeHist(gray.astype(np.uint8))
	blur = cv2.GaussianBlur(croppedImg, (5,5), 0)
	#img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	low_color = np.array([225,225,225])
	up_color = np.array([255,255,255])
	mask = cv2.inRange(blur, low_color, up_color)
	edges = cv2.Canny(mask, 75, 150)

	lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=50)
	if lines is not None:
		for line in lines:
			x1, y1, x2, y2 = line[0]
			cv2.line(croppedImg, (x1, y1), (x2, y2), (0,0,255), 5)
			#cv2.line(image_finale, (x1, y1), (x2, y2), (0,0,255), 5)
	
	cv2.imwrite("./image_coupe.jpg", croppedImg)
	#cv2.imwrite("./image_finale.jpg", image_finale)


detect_road()
