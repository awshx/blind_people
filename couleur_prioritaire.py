#!/usr/bin/python

import cv2
import numpy as np

def couleur_prio():

	image = cv2.imread('./logo/orange.jpg')
	frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	h = frame[:,:,0]
	s = frame[:,:,1]

	rouge = 0
	jaune = 0
	vert = 0
	cyan = 0
	bleu = 0
	magenta = 0
	orange = 0

	for index, element in enumerate(h):
		for index2, element2  in enumerate(element):
	
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

	tab = [rouge, jaune, vert, cyan, bleu, magenta, orange]
	tab.sort()
	print(tab)

	print("Couleur prioritaire:")
	if tab[6] == 0:
		cp = "blanc"
	elif tab[6] == rouge:
		cp = "rouge"
	elif tab[6] == jaune:
		cp = "jaune"
	elif tab[6] == vert:
		cp = "vert"
	elif tab[6] == cyan:
		cp = "cyan"
	elif tab[6] == bleu:
		cp = "bleu"
	elif tab[6] == magenta:
		cp = "magenta"
	elif tab[6] == orange:
                cp = "orange"

	print(cp)
	return cp

couleur_prio()
