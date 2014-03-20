#-*-coding:utf8-*-

import sys

class Capteur :

	def __init__(self,zones,vie) :
		
		self.zones = zones
		self.vie = vie

	def getZones(self) :
		print self.zones

	def setZones(self,zones) :
		self.zones = zones
		print "Champ 'zones' mis à jour."

	def getVie(self) :
		print self.vie

	def setVie(self,vie) :
		self.vie = vie
		print "Champ 'vie' mis à jour."