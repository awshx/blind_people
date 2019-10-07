<?php
// connexion à la base de données:
mysql_connect("localhost","root","Palace8313");
mysql_select_db("database_logo");
echo "Connexion a la database\n";

// récolte des données du fichier:
$image_tmp = $_FILES["image"]["tmp_name"];
$image_name = $_FILES["image"]["name"];
$image_size = $_FILES["image"]["size"];

// ajout dans la table:
$donnees = addslashes(fread(fopen($image_tmp, "r"), $image_size));
$id = mysql_insert_id();
$result = mysql_query("INSERT INTO logo (nom_image, donnees_binaires) VALUES ('$image_name', '$donnees')");
echo "\n\nInsertion dans la base de donnees\n";
mysql_close();
?>
