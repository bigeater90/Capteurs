#-*-coding:utf8-*-

from Capteur import *

capteurs = input("Nombre de capteurs à créer : ")

all_zones = []
all_vie = []

for i in range(1,capteurs) :
	i.zones = input("Entrez les zones : ")
	while not(isinstance(i.zones,list)) :
		print "Erreur premier paramètre : liste demandée."
		i.zones = input("Entrez les zones : ")

	i.vie = input("Entrez la durée de vie : ")
	while not(isinstance(i.vie,list)) :
		print "Erreur premier paramètre : liste demandée."
		i.vie = input("Entrez la durée de vie : ")

	all_zones.append(i.zones)
	all_vie.append(i.vie)


print all_zones
print all_vie






	
