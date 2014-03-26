#-*-coding:utf8-*-

import sys

class Capteur :

	def __init__(self,nombre,zones,vie) :
		
		self.nombre = nombre
		self.zones = zones
		self.vie = vie


	def show(self) :
		self.getZones()
		self.getVie()
