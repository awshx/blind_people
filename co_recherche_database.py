import mysql.connector 

test = "orange"
i = 0
tab = [0]*10

baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="database_logo")
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT lien FROM logo WHERE couleur_dominante LIKE '%" + test + "%'")
for ligne in curseur.fetchall():
	tab[i] = ligne
	i += 1

print(tab[0])

baseDeDonnees.close()
