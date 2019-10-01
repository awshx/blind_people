#!/usr/bin/python

import cv2

image = cv2.imread('test.png')


cv2.imshow("test", image) # creation d'une fenetre appelee test contenant image


cv2.waitKey(1000)# detruire la fenetre au bout d'une seconde
