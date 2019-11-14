import cv2
from matplotlib.pyplot import *
import numpy
import math

img1 = cv2.imread("../Images_rue/Image9.jpg")
blue,green,red = cv2.split(img1)

blur = cv2.GaussianBlur(img1, (5,5),0)
#hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
low_color = np.array([245, 245, 245])
up_color = np.array([255,255,255])
mask = cv2.inRange(blur, low_color, up_color)
edges = cv2.Canny(mask, 150, 200)

cv2.imwrite("./test.jpg", mask)
#cv2.imwrite("./testedges.jpg", hsv)

#lines = cv2.HoughLinesP(edges, 1, np.pi/180, 210, maxLineGap=50)
#if lines is not None:
	#for line in lines:
		#x1, y1, x2, y2 = line[0]
		#cv2.line(blur, (x1, y1), (x2, y2), (0,0,255), 5)

#cv2.imwrite("./detection_lignes_routes.jpg", blur)
