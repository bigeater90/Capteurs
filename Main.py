#-*-coding:utf8-*-

from Capteur import *

capteurs = input("Nombre de capteurs à créer : ")

all_capteurs = []
all_zones = []
all_vie = []

for i in range(1,capteurs+1) :

	val_zones = input("Entrez les zones : ")
	while not(isinstance(val_zones,list)) :
		print "Erreur premier paramètre : liste demandée."
		val_zones = input("Entrez les zones : ")

	val_vie = input("Entrez la durée de vie : ")
	while not(isinstance(val_vie,int)) :
		print "Erreur premier paramètre : liste demandée."
		val_vie = input("Entrez la durée de vie : ")

	capt = Capteur(val_zones,val_vie)

	all_capteurs.append(capt)

	for obj in all_capteurs :
		print "\n\n###Capteur ",all_capteurs.index(obj)+1," ### "
		print "Zones : ",obj.zones
		print "Durée de vie : ",obj.vie


	#print all_capteurs
# 	i.zones = input("Entrez les zones : ")
# 	while not(isinstance(i.zones,list)) :
# 		print "Erreur premier paramètre : liste demandée."
# 		i.zones = input("Entrez les zones : ")

# 	i.vie = input("Entrez la durée de vie : ")
# 	while not(isinstance(i.vie,list)) :
# 		print "Erreur premier paramètre : liste demandée."
# 		i.vie = input("Entrez la durée de vie : ")

# 	all_zones.append(i.zones)
# 	all_vie.append(i.vie)


# print all_zones
# print all_vie






	
