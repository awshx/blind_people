import mysql.connector 

test = "orange"

baseDeDonnees = mysql.connector.connect(host="localhost",user="root",password="root", database="database_logo")
curseur = baseDeDonnees.cursor()
curseur.execute("SELECT * FROM logo WHERE couleur_dominante LIKE '%" + test + "%'")
for ligne in curseur.fetchall():
	print(ligne)
