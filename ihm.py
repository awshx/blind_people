# coding: utf-8
 
from tkinter import * 
from tkinter.filedialog import *
import co_recherche_database as crb
import watershed as ws
from PIL import Image, ImageTk

def checkPicture():

	filename  = askopenfilename(title="Ouvrir votre image", filetypes=[('jpg files','.jpg')])

	fenetre3 = Tk()

	Canevas = Canvas(fenetre3) 
	photo = ImageTk.PhotoImage(file=filename)
	Canevas.config(height=photo.height(),width=photo.width())
	Canevas.create_image(0,0,anchor=NW,image=photo)
	Canevas.pack()   
	
	
	fenetre3.mainloop()

def route_trottoirs():
	
	print('Détection routes, trottoirs,...')

	#ws.legendes()
	#ws.watershed_detection()	

	fenetre2 = Tk()
	label = Label(fenetre2, text="Lancement programme: détection route/trottoir")
	label.pack(side=TOP, padx=25, pady=10)

	fenetre2.mainloop()


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
