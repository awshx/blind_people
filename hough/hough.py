import cv2
from matplotlib.pyplot import *
import numpy
import math

img1 = cv2.imread("../Images_rue/Image9.jpg")
blue,green,red = cv2.split(img1)

blur = cv2.GaussianBlur(img1, (5,5),0)
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
low_white = np.array([0, 0, 229])
up_white = np.array([180, 38, 255])
mask = cv2.inRange(hsv, low_white, up_white)
edges = cv2.Canny(mask, 75, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 210, maxLineGap=50)
if lines is not None:
	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv2.line(blur, (x1, y1), (x2, y2), (0,0,255), 5)

cv2.imwrite("./detection_lignes_routes.jpg", blur)
