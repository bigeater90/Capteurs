#-*-coding:utf8-*-

from Capteur import *
from random import *

all_capteurs = []
all_zones = []
all_vie = []

def choixUtilisateur():
	capteurs = input("Nombre de capteurs à créer : ")

	for i in range(1,capteurs+1) :
		
		print "\n\n### Capteur",i,"###	 "
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
		
		print "\n"
		for obj in all_capteurs :
			print "### Capteur",all_capteurs.index(obj)+1,"###"
			obj.show()


def choixAleatoire() :
	capteurs = randint(1,10)					# on crée aléatoirement de 1 à 10 capteurs
	nbZones = randint(1,10)  					# on crée aléatoirement de 1 à 10 zones

	
	
	# START DEBUG PART 
	print "capteurs : " , capteurs
	print " nbZones : " , nbZones
	print
	# END DEBUG PART
	
	for i in range(1,capteurs+1) :
		val_vie = randint(1,10) 					# on crée aléatoirement une durée de vie de 1 à 10 unités
		val_zones = []
		nbZonesCapteur = randint(1,nbZones)		# on sélectionne le nombre de zones surveillés par le capteur
		for j in range(1,nbZonesCapteur+1) :
			a = randint(1,nbZones)
			if a not in val_zones :
				val_zones.append(a) 			# on sélectionne les zones surveillés en fonction de nbZonesCapteur
	
		# START DEBUG PART	
# 		print "capteur " , i
# 		print "------------"
# 		print " zones : " , val_zones
# 		print " durée de vie : " , vie
# 		print
		# END DEBUG PART
		
		capt = Capteur(val_zones,val_vie)

		all_capteurs.append(capt)

	for obj in all_capteurs :
		print "\n\n###Capteur ",all_capteurs.index(obj)+1," ### "
		print "Zones : ",obj.zones
		print "Durée de vie : ",obj.vie
		
choixAleatoire()