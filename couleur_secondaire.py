#!/usr/bin/python

import cv2
import numpy as np

def couleur_second():

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

	for index, element in enumerate(h):
		for index2, element2  in enumerate(element):
	
			if s[index][index2] < 100:
				continue
			if element2>(329/2) or element2<(30/2):
				rouge += 1
			if element2>29/2 and element2<90/2:
				jaune += 1
			if element2>89/2 and element2<150/2:
				vert += 1
			if element2>149/2 and element2<210/2:
				cyan += 1
			if element2>209/2 and element2<270/2:
				bleu += 1
			if element2>269/2 and element2<330/2:
				magenta += 1

	tab = [rouge, jaune, vert, cyan, bleu, magenta]
	tab.sort()
	print(tab)

	print("Couleur secondaire:")
	if tab[4] == 0:
		cs = "blanc"
	elif tab[4] == rouge:
		cs = "rouge"
	elif tab[4] == jaune:
		cs = "jaune"
	elif tab[4] == vert:
		cs = "vert"
	elif tab[4] == cyan:
		cs = "cyan"
	elif tab[4] == bleu:
		cs = "bleu"
	elif tab[4] == magenta:
		cs = "magenta"

	print(cs)
	return cs

couleur_second()
