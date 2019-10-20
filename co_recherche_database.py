import mysql.connector
import cv2
import numpy as np
 
import couleur_prioritaire as cp
import couleur_secondaire as cs
import reconnaissance_logo as rl

query_image = cv2.imread('./logo/orange.jpg')

nb_noms = 0
nb_liens = 0
tab_nom_logo = [0]*10
tab_logo = [0]*10

baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="database_logo")

print("Recherche de la couleur dominante")
prioritaire = cp.couleur_prio(query_image)
print("Recherche de la couleur secondaire")
secondaire = cs.couleur_second(query_image)

curseur = baseDeDonnees.cursor()
curseur.execute("SELECT nom_image FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")

for nom in curseur.fetchall():
	tab_nom_logo[nb_noms] = nom
	nb_noms += 1

curseur.execute("SELECT lien FROM logo WHERE couleur_dominante LIKE '%" + prioritaire + "%' AND couleur_secondaire LIKE '%" + secondaire + "%' ")

for lien in curseur.fetchall():
        tab_logo[nb_liens] = lien
        nb_liens += 1

baseDeDonnees.close()

logo_final = rl.reco_logo(query_image, tab_nom_logo, tab_logo, nb_noms, nb_liens)
print(logo_final)

