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

		capt = Capteur(i,val_zones,val_vie)

		all_capteurs.append(capt)
		
		print 
		for obj in all_capteurs :
			print "### Capteur",i,"###"
			obj.show()


def choixAleatoire() :
	capteurs = randint(1,10)					# on crée aléatoirement de 1 à 10 capteurs
	nbZones = randint(1,10)  					# on crée aléatoirement de 1 à 10 zones

	
	

	print "capteurs : " , capteurs
	print " nbZones : " , nbZones
	print
	
	for i in range(1,capteurs+1) :
		val_vie = randint(1,10) 					# on crée aléatoirement une durée de vie de 1 à 10 unités
		val_zones = []
		nbZonesCapteur = randint(1,nbZones)		# on sélectionne le nombre de zones surveillées par le capteur
		for j in range(1,nbZonesCapteur+1) :
			a = randint(1,nbZones)
			if a not in val_zones :
				val_zones.append(a) 			# on sélectionne les zones surveillées en fonction de nbZonesCapteur
	
		capt = Capteur(i,val_zones,val_vie)

		all_capteurs.append(capt)

	for obj in all_capteurs :
		print "\n\n### Capteur ",obj.nombre," ### "
		print "Zones : ",obj.zones
		print "Durée de vie : ",obj.vie
		



def conf_elems() :

	tous_les_capteurs = [Capteur(1,[2],5), Capteur(2,[2,3,4],6), Capteur(3,[1,3],7), Capteur(4,[1,3,4],8)]
	toutes_les_zones = [1,2,3,4]
	zones_actuelles = []
	capteurs_utilises = []
	conf_elems = []
	elem = []
	# for i in tous_les_capteurs :
	# 	while toutes_les_zones != zones_actuelles :
	# 		for j in i.zones :
	# 			if j not in zones_actuelles :
	# 				zones_actuelles.append(j)
	# 		capteurs_utilises.append(i.nombre)

	fin_capteurs = False

	while zones_actuelles != toutes_les_zones  and not fin_capteurs:

		for i in tous_les_capteurs :
			print "New i : ",i.nombre
			for j in tous_les_capteurs[tous_les_capteurs.index(i):] :
				print "j : ",j.nombre
				for k in i.zones :
					if k not in zones_actuelles :
						zones_actuelles.append(k)
						if i.nombre not in capteurs_utilises :
							capteurs_utilises.append(i.nombre)

				if capteurs_utilises not in conf_elems :
					conf_elems.append(capteurs_utilises)

		fin_capteurs = True
	
	print "zones couvertes : ",zones_actuelles
	print "capteurs utilisés : ", capteurs_utilises
	print "configurations élémentaires : ",conf_elems



#choixAleatoire()

conf_elems()







