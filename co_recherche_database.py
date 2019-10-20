import mysql.connector
import cv2
import numpy as np
 
import couleur_prioritaire as cp
import couleur_secondaire as cs
import reconnaissance_logo as rl

query_image = cv2.imread('./logo/orange.jpg')

nb_noms = 0
nb_liens = 0
tab_nom_logo = []
tab_logo = []

baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="database_logo")

print("Recherche de la couleur dominante")
prioritaire = cp.couleur_prio(query_image)
print("Recherche de la couleur secondaire")
secondaire = cs.couleur_second(query_image)

curseur = baseDeDonnees.cursor()

query_nom_image = ("SELECT nom_image FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")
curseur.execute(query_nom_image)

for nom_image in curseur:
	tab_nom_logo.append(nom_image)
	nb_noms += 1

liste = list(tab_nom_logo)
liste[0].remove("u") 
print(liste[0])

query_lien = ("SELECT lien FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")
curseur.execute(query_lien)

for lien in curseur:
        tab_logo.append(lien)
        nb_liens += 1
#print(tab_logo)

baseDeDonnees.close()

#logo_final = rl.reco_logo(query_image, tab_nom_logo, tab_logo, nb_noms, nb_liens)
#print(logo_final)

