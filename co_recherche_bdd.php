#!/usr/bin/php

<?php
#Tentative de connexion a la database

$link = mysqli_connect("localhost", "root", "root", "database_logo");

if (!$link) { #Erreur lors de la tentative de connexion
        echo "Erreur: Impossible de se connecter à MySQL" . PHP_EOL;
        echo "Erno de débogage : " . mysqli_connect_errno() . PHP_EOL;
        echo "Erreur de débogage : " . mysqli_connect_error() . PHP_EOL;
        exit;
}

#Une connexion reussie et l'utilisateur peut entrer sa recherche dans la console
echo "Succès : Une connexion correcte à MySQL a été faite!\n" . PHP_EOL;
echo "Lancement des scripts python";
$query_couleur = exec("python couleur_prioritaire.py 2>&1");
$query_couleur_second = exec("python couleur_secondaire.py 2>&1");
echo "\nFin des scripts python";
$clean_query_couleur = trim($query_couleur);
$clean_query_couleur_second = trim($query_couleur_second);
echo "\nCouleur prioritaire:";
echo $clean_query_couleur."\n";
echo "Couleur secondaire:";
echo $clean_query_couleur_second."\n";
$min_length = 0;

#Condition pour voir si la chaine de caractere entre par l'utilisateur est plus grand que la taille minimale demande (a savoir un caractere)
if(strlen($clean_query_couleur) >= $min_length && strlen($clean_query_couleur_second)) {
	$clean_query_couleur = htmlspecialchars($clean_query_couleur);
        $clean_query_couleur = mysqli_real_escape_string($link, $clean_query_couleur);
	$clean_query_couleur_second = htmlspecialchars($clean_query_couleur_second);
        $clean_query_couleur_second = mysqli_real_escape_string($link, $clean_query_couleur_second);




			#Recherche dans la database par rapport a la chaine de l'utilisateur
                        $raw_results = mysqli_query($link,"SELECT * FROM logo WHERE (`couleur_dominante` LIKE '%$clean_query_couleur%') AND (`couleur_secondaire` LIKE '%$clean_query_couleur_second%')");
                        if(mysqli_num_rows($raw_results) > 0) { #On affiche les resultats trouve a l'utilisateur
                                while($results = mysqli_fetch_array($raw_results)) {
                                        echo "\nId:".$results['id']." Nom:".$results['nom_image']." Lien:".$results['lien']." Couleur dominante:".$results['couleur_dominante']." Couleur secondaire:".$results['couleur_secondaire']."\n";
                                }
                        }
                        else {
                                echo "Pas de resultats";
                        }
                }
else {
	echo "La taille minimum de la recherche: ".$min_length;
     }

#On ferme la connexion avec la database
mysqli_close($link);

?>
