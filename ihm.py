# coding: utf-8
 
from tkinter import * 
from tkinter.filedialog import *
import co_recherche_database as crb
import watershed as ws
from PIL import Image, ImageTk
import cv2

def route_trottoirs():
	
	print('Détection routes, trottoirs,...')

	ws.legendes()
	ws.watershed_detection()	


def enseignes():
	
	print('Reconnaissance logo sur une image')
	crb.recherche_logo()
	

def menu_principal():

	fenetre = Tk()

	label = Label(fenetre, text="Blind People !")
	label.pack(side=TOP, padx=25, pady=10)

	lf = LabelFrame(fenetre, padx=25, pady=25)
	lf.pack(fill="both", expand="yes")

	Button(lf, text ='Détection routes/trottoirs', command=route_trottoirs).pack(side=LEFT, padx=25, pady=25)
	Button(lf, text ='Reconnaissance logo', command=enseignes).pack(side=RIGHT, padx=25, pady=25)

	fenetre.mainloop()

menu_principal()
