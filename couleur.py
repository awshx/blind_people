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
			if v[index][index2] < 20:
				noir += 1
				continue
			if s[index][index2] < 100:
				continue
			if element2>(329/2) or element2<(19/2):
				rouge += 1
			if element2>20/2 and element2<29/2: #de base 49/2
				orange += 1
			if element2>30/2 and element2<90/2: #de base 50/2
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
	tab.sort()
	print(tab)

	if tab[7] == 0:
		cp = "blanc"
	elif tab[7] == rouge:
		cp = "rouge"
	elif tab[7] == jaune:
		cp = "jaune"
	elif tab[7] == vert:
		cp = "vert"
	elif tab[7] == cyan:
		cp = "cyan"
	elif tab[7] == bleu:
		cp = "bleu"
	elif tab[7] == magenta:
		cp = "magenta"
	elif tab[7] == orange:
                cp = "orange"
	elif tab[7] == noir:
		cp = "noir"

	if tab[6] == 0:
		cs = "blanc"
	elif tab[6] == rouge:
		cs = "rouge"
	elif tab[6] == jaune:
		cs = "jaune"
	elif tab[6] == vert:
		cs = "vert"
	elif tab[6] == cyan:
		cs = "cyan"
	elif tab[6] == bleu:
		cs = "bleu"
	elif tab[6] == magenta:
		cs = "magenta"
	elif tab[6] == orange:
		cs = "orange"
	elif tab[6] == noir:
		cs = "noir"

	
	print("Couleur prioritaire: " + cp)
	print("Couleur secondaire: " + cs)
	tab_couleur = []
	tab_couleur.append(cp)
	tab_couleur.append(cs)
	
	return tab_couleur
