#!/usr/bin/python

import cv2
import numpy as np

def couleur(image):

	frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	h = frame[:,:,0]
	s = frame[:,:,1]
	v = frame[:,:,2]
    
	rouge = 0
	jaune = 0
	vert = 0
	cyan = 0
	bleu = 0
	magenta = 0
	orange = 0
	noir = 0

	for index, element in enumerate(h):
		for index2, element2  in enumerate(element):
			if s[index][index2] < 20:
                		noir +=1
                		continue
			if s[index][index2] < 100:
				continue
			if element2>(329/2) or element2<(19/2):
				rouge += 1
			if element2>20/2 and element2<49/2:
				orange += 1
			if element2>50/2 and element2<90/2:
				jaune += 1
			if element2>89/2 and element2<150/2:
				vert += 1
			if element2>149/2 and element2<210/2:
				cyan += 1
			if element2>209/2 and element2<270/2:
				bleu += 1
			if element2>269/2 and element2<330/2:
				magenta += 1

	tab = [rouge, jaune, vert, cyan, bleu, magenta, orange, noir]
	couleurs = ["rouge", "jaune", "vert", "cyan", "bleu", "magenta", "orange", "noir"]
	print(tab)
    
    	maxValueIndex = tab.index(max(tab))
    	
    	cp = couleurs[maxValueIndex]
	print(cp)
    	tab.pop(maxValueIndex)
    	couleurs.pop(maxValueIndex)
    	cs = couleurs[tab.index(max(tab))]
    
	print("Couleur prioritaire: " + cp)
	print("Couleur secondaire: " + cs)
	tab_couleur = []
	tab_couleur.append(cp)
	tab_couleur.append(cs)
	
	return tab_couleur
