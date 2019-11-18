# coding: utf-8
 
from tkinter import * 
from tkinter.filedialog import *

def checkPicture():
	filename  = askopenfilename(title="Ouvrir votre image", filetypes=[('all files','.*')])
	fichier = open(filename, "r")
	content = fichier.read()

	fenetre3 = Tk()
	Label(fenetre3, text=content).pack()
	
	
	fenetre3.mainloop()

def route_trottoirs():
	print('route_trottoirs')
	fenetre2 = Tk()
	label = Label(fenetre2, text="Lancement programme: detection route_trottoirs")
	label.pack(side=TOP, padx=25, pady=10)

	Button(fenetre2, text ='find picture', command=checkPicture).pack(padx=25, pady=25)

	fenetre2.mainloop()

def enseignes():
	print('enseignes')

fenetre = Tk()

label = Label(fenetre, text="Blind People !")
label.pack(side=TOP, padx=25, pady=10)

lf = LabelFrame(fenetre, padx=25, pady=25)
lf.pack(fill="both", expand="yes")

Button(lf, text ='routes / trottoirs', command=route_trottoirs).pack(side=LEFT, padx=25, pady=25)
Button(lf, text ='enseignes / logos', command=enseignes).pack(side=RIGHT, padx=25, pady=25)


fenetre.mainloop()