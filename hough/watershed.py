import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils
import time

def invert_img(img):
    img = (255-img)
    return img

def legendes():

	#i = 0
	classes = []	
	couleurs = []

	with open("./classes.txt", "r") as fichier_classes:
		for line in fichier_classes.readlines():
			une_ligne = line.split()
			classes.append(une_ligne)
	fichier_classes.close()

	with open("./couleurs.txt", "r") as fichier_couleurs:
                for line in fichier_couleurs.readlines():
                        une_ligne = line.split()
                        couleurs.append(une_ligne)
			#print(couleurs[i])
			#i = i+1
        fichier_couleurs.close()

	#print(couleurs)

	legend = np.zeros(((len(classes) * 60) + 50, 400, 3), dtype="uint8")
	for (i, (className, c)) in enumerate(zip(classes, couleurs)):
		# draw the class name + color on the legend
		className = str(classes[i]) 
		couleur = [int(j) for j in c]
		#print(className)
		#print(couleur)
		cv2.putText(legend, className, (0, (i * 75)+50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
		cv2.rectangle(legend, (125, (i * 75)+60), (525, (i * 75)+30), couleur, -1)

	cv2.imwrite("./legendes.jpg", legend)

def watershed():

	img = cv2.imread("../Images_rue/Image9.jpg")
	mask = cv2.imread("../Images_rue/Image9.jpg")
	img = imutils.resize(img, height = 300)
        mask = imutils.resize(mask, height = 300)

	gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

	ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	thresh = invert_img(thresh)

# Suppression du bruit
	kernel = np.ones((3,3), np.uint8)
	opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 4)

# Recherche de l'arriere plan
	sure_bg = cv2.dilate(opening,kernel,iterations=3)

# Recherche du plan de devant
	dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
	ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Recherche des regions inconnus
	sure_fg = np.uint8(sure_fg)
	unknown = cv2.subtract(sure_bg,sure_fg)

	ret, markers = cv2.connectedComponents(sure_fg)
	markers = markers+1

# Les regions inconnus ont une marque a 0
	markers[unknown==255] = 0

# Mise en place du watershed
	markers = cv2.watershed(mask,markers)
	mask[markers == -1] = [0,0,255]
	mask[markers == 2] = [0,0,255]
	mask[markers == 1] = [255,255,255]

	result = ((0.4 * img) + (0.6 * mask)).astype("uint8")	

	cv2.imwrite('./background.jpg', sure_bg)
	cv2.imwrite('./foreground.jpg', sure_fg)
	cv2.imwrite('./threshold.jpg', thresh)
	cv2.imwrite('./mask.jpg', mask)
	cv2.imwrite('./img.jpg', img)
	cv2.imwrite('./result.jpg', result)

legendes()
watershed()
