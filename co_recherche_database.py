import mysql.connector
import cv2
import numpy as np
 
import couleur as coul
import reconnaissance_logo as rl
import detection_forme as df
import pts_communs as pc

tab_query_image = []

tab_query_image = df.detect_shape()
query_image = cv2.imread(tab_query_image[0])

nb_noms = 0
nb_liens = 0
tab_nom_logo = []
tab_logo = []

if tab_query_image[0] == '0':
	print("Pas de formes détectées")
	print("Fin de la recherche")

elif tab_query_image[0] != '0':
	baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="database_logo")

	print("Recherche de la couleur dominante et secondaire")
	color = []
	color = coul.couleur(query_image)
	prioritaire = color[0]
	secondaire = color[1]

	curseur = baseDeDonnees.cursor()

	query_nom_image = ("SELECT nom_image FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")
	curseur.execute(query_nom_image)

	for nom_image in curseur:
		tab_nom_logo.append(nom_image)
		nb_noms += 1

	liste_nom = [] 
	# initialisation de liste
	for tuple_nom in tab_nom_logo: 
    		for i in tuple_nom: 
        		liste_nom.append(i) 
  
	# afficher la liste
	for i in range(nb_noms):
		liste_nom[i] = liste_nom[i].encode('utf8')
	print(liste_nom) 

	query_lien = ("SELECT lien FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")
	curseur.execute(query_lien)

	for lien in curseur:
        	tab_logo.append(lien)
        	nb_liens += 1

	liste_lien = []
	# initialisation de liste
	for tuple_lien in tab_logo:
    		for i in tuple_lien:
        		liste_lien.append(i)

	# afficher la liste
	for i in range(nb_noms):
        	liste_lien[i] = liste_lien[i].encode('utf8')
	print(liste_lien)


	baseDeDonnees.close()

	logo_final = rl.reco_logo(query_image, liste_nom, liste_lien, nb_noms, nb_liens)
	print("Le logo reconnu: " + logo_final)

	coordo = []
	coordo = df.coordonnees_centrale_logo()
	image_etiquette = cv2.imread('./Images_detection_formes/coordoCentrale.jpg')
	pc.label(image_etiquette, logo_final, coordo)
	cv2.imwrite('./etiquette.jpg', image_etiquette)
