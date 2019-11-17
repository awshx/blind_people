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

	choix_image = "../Images_rue/Image9.jpg"
	img = cv2.imread(choix_image)
	mask_route = cv2.imread(choix_image)
	mask_trottoir = cv2.imread(choix_image)
	
	img = imutils.resize(img, height = 300)
        mask_route = imutils.resize(mask_route, height = 300)
	mask_trottoir = imutils.resize(mask_trottoir, height = 300)

	gray_route = cv2.cvtColor(mask_route, cv2.COLOR_BGR2GRAY)
	gray_trottoir = cv2.cvtColor(mask_trottoir, cv2.COLOR_BGR2GRAY)

	ret_route, thresh_route = cv2.threshold(gray_route,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
	ret_trottoir, thresh_trottoir = cv2.threshold(gray_trottoir,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

	thresh_route = invert_img(thresh_route)

# Suppression du bruit
	kernel = np.ones((3,3), np.uint8)
	opening_route = cv2.morphologyEx(thresh_route,cv2.MORPH_OPEN,kernel, iterations = 4)
	opening_trottoir = cv2.morphologyEx(thresh_trottoir,cv2.MORPH_OPEN,kernel, iterations = 4)

# Recherche de l'arriere plan
	sure_bg_route = cv2.dilate(opening_route,kernel,iterations=3)
	sure_bg_trottoir = cv2.dilate(opening_trottoir,kernel,iterations=3)
	
# Recherche du plan de devant
	dist_transform_route = cv2.distanceTransform(opening_route, cv2.DIST_L2, 5)
	ret_route, sure_fg_route = cv2.threshold(dist_transform_route,0.7*dist_transform_route.max(),255,0)
	dist_transform_trottoir = cv2.distanceTransform(opening_trottoir, cv2.DIST_L2, 5)
        ret_trottoir, sure_fg_trottoir = cv2.threshold(dist_transform_trottoir,0.7*dist_transform_trottoir.max(),255,0)

# Recherche des regions inconnus
	sure_fg_route = np.uint8(sure_fg_route)
	unknown_route = cv2.subtract(sure_bg_route,sure_fg_route)
	sure_fg_trottoir = np.uint8(sure_fg_trottoir)
        unknown_trottoir = cv2.subtract(sure_bg_trottoir,sure_fg_trottoir)

	ret_route, markers_route = cv2.connectedComponents(sure_fg_route)
	markers_route = markers_route+1
	ret_trottoir, markers_trottoir = cv2.connectedComponents(sure_fg_trottoir)
        markers_trottoir = markers_trottoir+1

# Les regions inconnus ont une marque a 0
	markers_route[unknown_route == 255] = 0
	markers_trottoir[unknown_trottoir == 255] = 0

# Mise en place du watershed
	markers_route = cv2.watershed(mask_route,markers_route)
	mask_route[markers_route == -1] = [0,0,255]
	mask_route[markers_route == 2] = [0,0,255]
	mask_route[markers_route == 1] = [255,255,255]
	markers_trottoir = cv2.watershed(mask_trottoir,markers_trottoir)
        mask_trottoir[markers_trottoir == -1] = [0,255,0]
        mask_trottoir[markers_trottoir == 2] = [0,255,0]
        mask_trottoir[markers_trottoir == 1] = [255,255,255]

	result_route = ((0.4 * img) + (0.6 * mask_route)).astype("uint8")	
	result_trottoir = ((0.4 * img) + (0.6 * mask_trottoir)).astype("uint8")
	result = ((0.5 * result_route) + (0.5 * result_trottoir)).astype("uint8")

	#cv2.imwrite('./background.jpg', sure_bg)
	#cv2.imwrite('./foreground.jpg', sure_fg)
	#cv2.imwrite('./threshold.jpg', thresh)
	cv2.imwrite('./img.jpg', img)
	cv2.imwrite('./mask_route.jpg', mask_route)
	cv2.imwrite('./mask_trottoir.jpg', mask_trottoir)
	cv2.imwrite('./result_route.jpg', result_route)
	cv2.imwrite('./result_trottoir.jpg', result_trottoir)
	cv2.imwrite('./result.jpg', result)

legendes()
watershed()
