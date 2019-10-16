#!/usr/bin/python

import cv2
import numpy as np

def couleur_prio():

	image = cv2.imread('./logo/mcdo.jpg')
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

	print("Couleur prioritaire:")
	if tab[5] == 0:
		cp = "blanc"
	if tab[5] == rouge:
		cp = "rouge"
	if tab[5] == jaune:
		cp = "jaune"
	if tab[5] == vert:
		cp = "vert"
	if tab[5] == cyan:
		cp = "cyan"
	if tab[5] == bleu:
		cp = "bleu"
	if tab[5] == magenta:
		cp = "magenta"

	print(cp)
	return cp

couleur_prio()
