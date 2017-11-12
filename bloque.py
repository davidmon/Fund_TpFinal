# -*- coding: utf-8 -*-

import graphics as g
import configuracion as c

coloresEstado = {'susceptible': c.colorBlueS, 'infectada': c.colorRedI, 'recuperada': c.colorGreenR, 'muerta': c.colorWhiteM}

class Bloque():

	def __init__(self, tablero, celda):		
		self.tablero = tablero
		self.celda = celda
		self.cantVecinosInfectados = 0
		self.cantDiasInfectada = 0
		self.estadoactual = "susceptible"
		self.estadoFuturo = "susceptible"
		self.vecinos = []
		

	def evaluate(self, infeccion, recuperacion, cantDiasInfeccion):
		if self.estadoactual == "susceptible":
			for x in range(0, len(self.vecinos)):
				vecino = self.tablero.retornarVecino(self.vecinos[x])
				if vecino.estadoactual == "infectada":
					self.cantVecinosInfectados += 1
			if self.cantVecinosInfectados > 0:
				for inf in range (0,self.cantVecinosInfectados):
					if self.estadoFuturo == "susceptible":
						if infeccion.rvs() == 0:
							self.estadoFuturo = "infectada"
							self.tablero.cantidadS -= 1
							self.tablero.cantidadI += 1
			self.cantVecinosInfectados = 0
		if self.estadoactual == "infectada":
			if self.cantDiasInfectada <= cantDiasInfeccion:
				self.cantDiasInfectada += 1
				if recuperacion.rvs() == 2:
					self.estadoFuturo = "recuperada"
					self.tablero.cantidadR += 1
					self.tablero.cantidadI -= 1
				else:
					self.estadoFuturo  = "infectada"
			else:
				self.estadoFuturo = "muerta"
				self.tablero.cantidadM += 1
				self.tablero.cantidadI -= 1
		

	def actualizate(self):
		self.estadoactual = self.estadoFuturo
		self.celda.setFill(coloresEstado[self.estadoactual])
		