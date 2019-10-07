create database if not exists database_logo; -- créer une database si elle n'existe pas
use database_logo; -- on utilise cette databse

drop table if exists logo; -- on supprime la table logo de cette database si elle existe
create table if not exists logo ( -- on creee la table logo si elle n'existe pas
	id smallint unsigned not null auto_increment, -- id est la primary key qui s'incremente automatiquement
	nom_image varchar(255) not null,
	donnees_binaires longblob not null,
	couleur varchar(40),
	primary key (id)
);
