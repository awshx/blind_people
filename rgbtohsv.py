import cv2
import numpy as np

image = cv2.imread('crab.bmp')
frame = cv2.cvtColor(image, cv.COLOR_BGR2HSV)

h = frame[:,:,0]

rouge = 0
jaune = 0
vert = 0
cyan = 0
bleu = 0
magenta = 0

for i in h:
	for j in i:
		if j == 0:
			continue
		if j>329/2 or j<30/2:
			rouge += 1
		if j>29/2 and j<90/2:
			jaune += 1
		if j>89/2 and j<150/2:
			vert += 1
		if j>149/2 and j<210/2:
			cyan += 1
		if j>209/2 and j<270/2:
			bleu += 1
		if j>269/2 and j<330/2:
			magenta += 1

m = np.argmax((rouge, jaune, vert, cyan, bleu, magenta))

if m == 0:
	print("rouge")
if m == 1:
	print("jaune")
if m == 2:
	print("vert")
if m == 3:
	print("cyan")
if m == 4:
	print("bleu")
if m == 5:
	print("magenta")

cv2.imshow("crab",image)
cv2.waitkey(0)
