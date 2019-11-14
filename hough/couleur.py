#!/usr/bin/python

import cv2
import numpy as np

def couleur():

	image = cv2.imread("../Images_rue/Image9.jpg")
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
	
	img = np.array(image)

	for index, element in enumerate(h):
		for index2, element2  in enumerate(element):
			if v[index][index2] < 20:
                		noir += 1
				img[index][index2] = (255,255,255)
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
	print(tab)
	cv2.imwrite("./test.jpg", img)

couleur()
