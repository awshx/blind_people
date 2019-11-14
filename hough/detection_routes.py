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

	croppedImg = image[heightCropped:heightCropped*2,widthCropped:widthCropped*2]
	#cv2.imwrite("./test.jpg", croppedImg)

	return croppedImg

def detect_road():

	croppedImg = imageCenter()
	
	#gray = cv2.cvtColor(croppedImg, cv2.COLOR_BGR2GRAY)
	#gray = cv2.equalizeHist(gray.astype(np.uint8))
	blur = cv2.GaussianBlur(croppedImg, (5,5), 0)
	#img = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	low_color = np.array([200,200,200])
	up_color = np.array([255,255,255])
	mask = cv2.inRange(blur, low_color, up_color)
	
	cv2.imwrite("./test.jpg", mask)


detect_road()
