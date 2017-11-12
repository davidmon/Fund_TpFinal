# -*- coding: utf-8 -*-

import graphics as g
import tablero as t
import configuracion as c
import time
import scipy
from scipy import stats

class Ventana():
	
	def __init__(self):
		self.iteraciones = 40
		self.cantInfectados = 5
		self.coefVirulencia = 0.34
		self.coefRecuperacion = 0.6
		self.cantidadI = 0
		self.tic = 0
		self.cantDiasInfeccion = 3


	def graficar(self):	
		#ventana
		self.win = g.GraphWin("FTI - TPFinal", c.anchoVentana, c.altoVentana)
		self.win.setBackground(c.colorFondo)
		#header ventana
		self.pto0Header = g.Point(0,0)
		self.header = g.Rectangle(c.pto0Header,g.Point(c.pto0Header.getX()+c.anchoVentana,c.pto0Header.getY()+c.altoH))
		self.header.setFill(c.colorHeader)
		self.header.setOutline(c.colorHeader)
		self.header.draw(self.win)
		self.titulo = g.Text(g.Point(self.win.getWidth()/2, 13), 'Simulación Epidemia - Modelo SIR')
		self.titulo.setTextColor('white')
		self.titulo.setSize(11)
		self.titulo.draw(self.win)
		# grupo inputs
		self.inputs = g.Rectangle(c.pto0Input,g.Point(c.pto0Input.getX()+c.anchoI,c.pto0Input.getY()+c.altoI))
		self.inputs.setFill(c.colorWhiteM)
		self.inputs.setOutline(c.colorFondo)
		self.inputs.draw(self.win)
		# titulo inputs
		self.labelInput = g.Text(c.pto0LInput, 'VALORES DE ENTRADA')
		self.labelInput.setSize(9)
		self.labelInput.draw(self.win)
		#inputs
		self.inputBoxAlfa = g.Entry(c.ptOInputBoxAlfa, c.anchoInput)
		self.inputBoxAlfa.setFill(c.colorInput)
		self.inputBoxAlfa.setSize(10)
		self.inputBoxAlfa.draw(self.win)
		self.inputBoxAlfa.setText(self.coefVirulencia)
		self.inputBoxBeta = g.Entry(c.ptOInputBoxBeta, c.anchoInput)
		self.inputBoxBeta.setFill(c.colorInput)
		self.inputBoxBeta.setSize(10)
		self.inputBoxBeta.draw(self.win)
		self.inputBoxBeta.setText(self.coefRecuperacion)
		self.inputDuracionInfeccion = g.Entry(c.ptODurInfeccion, c.anchoInput)
		self.inputDuracionInfeccion.setFill(c.colorInput)
		self.inputDuracionInfeccion.setSize(10)
		self.inputDuracionInfeccion.draw(self.win)
		self.inputDuracionInfeccion.setText(self.cantDiasInfeccion)
		self.inputCantIteraciones = g.Entry(c.ptOInputCantIteraciones, c.anchoInput)
		self.inputCantIteraciones.setFill(c.colorInput)
		self.inputCantIteraciones.setSize(10)
		self.inputCantIteraciones.draw(self.win)
		self.inputCantIteraciones.setText(self.iteraciones)
		self.inputCantMaxInfectados = g.Entry(c.ptOInputCantFilas, c.anchoInput)
		self.inputCantMaxInfectados.setFill(c.colorInput)
		self.inputCantMaxInfectados.setSize(10)
		self.inputCantMaxInfectados.draw(self.win)
		self.inputCantMaxInfectados.setText(self.cantInfectados)
		# label inputs
		self.etiquetaInputBoxAlfa = g.Text(c.ptOLInputBoxAlfa,'Coef Virulencia:')
		self.etiquetaInputBoxAlfa.setSize(10)
		self.etiquetaInputBoxAlfa.draw(self.win)
		self.etiquetaInputBoxBeta = g.Text(c.ptOLInputBoxBeta,'Coef Recuperación:')
		self.etiquetaInputBoxBeta.setSize(10)
		self.etiquetaInputBoxBeta.draw(self.win)
		self.etiquetaInputBoxDInf = g.Text(c.ptOLInputDiasInF,'Duración Infección:')
		self.etiquetaInputBoxDInf.setSize(10)
		self.etiquetaInputBoxDInf.draw(self.win)
		self.etiquetaInputBoxIteraciones = g.Text(c.ptOLInputCantIteraciones,'Cant Iteraciones:')
		self.etiquetaInputBoxIteraciones.setSize(10)
		self.etiquetaInputBoxIteraciones.draw(self.win)
		self.etiquetaInputBoxInfectados = g.Text(c.ptOLInputCantFilas,'Cant Infectados:')
		self.etiquetaInputBoxInfectados.setSize(10)
		self.etiquetaInputBoxInfectados.draw(self.win)
		# grupo notificacion
		self.grafica = g.Rectangle(c.pto0Notif,g.Point(c.pto0Notif.getX()+c.anchoN,c.pto0Notif.getY()+c.altoN))
		self.grafica.setFill(c.colorWhiteM)
		self.grafica.setOutline(c.colorFondo)
		self.grafica.draw(self.win)
		# boton aceptar
		self.botonIniciar = g.Rectangle(c.pto0Boton,c.pto1Boton)
		self.botonIniciar.setFill(c.colorWhiteM)
		self.botonIniciar.setOutline(c.colorGreenBoton)
		self.botonIniciar.setWidth(2)
		self.botonIniciar.draw(self.win)
		self.etiquetaBoton = g.Text(c.pto0LBoton, 'INICIAR')
		self.etiquetaBoton.setSize(10)
		self.etiquetaBoton.setFill(c.colorGreenBoton)
		self.etiquetaBoton.draw(self.win)
		# mensaje
		self.message = g.Text(c.pto0Mensaje,'Iniciar Simulación del Modelo')
		self.message.setSize(12)
		self.message.draw(self.win)
		# iteraciones
		self.etiquetaIteracion = g.Text(c.pto0NotifIt,'Iteracion n°: -')
		self.etiquetaIteracion.setSize(10)
		self.etiquetaIteracion.draw(self.win)
		# cantidad S
		self.etiquetaS = g.Text(c.pto0NotifS,'Susceptibles: -')
		self.etiquetaS.setSize(10)
		self.etiquetaS.draw(self.win)
		# cantidad I
		self.etiquetaI = g.Text(c.pto0NotifI, 'Infectados: -')
		self.etiquetaI.setSize(10)
		self.etiquetaI.draw(self.win)
		# cantidad R
		self.etiquetaR = g.Text(c.pto0NotifR, 'Recuperados: -')
		self.etiquetaR.setSize(10)
		self.etiquetaR.draw(self.win)
		# cantidad M
		self.etiquetaM = g.Text(c.pto0NotifM, 'Muertos: -')
		self.etiquetaM.setSize(10)
		self.etiquetaM.draw(self.win)
		# id cantidad S
		self.cuadroS = g.Rectangle(c.pto0CuadroS,c.pto1CuadroS)
		self.cuadroS.setFill(c.colorBlueS)
		self.cuadroS.setOutline(c.colorBlueS)
		self.cuadroS.draw(self.win)
		# id cantidad I
		self.cuadroI = g.Rectangle(c.pto0CuadroI,c.pto1CuadroI)
		self.cuadroI.setFill(c.colorRedI)
		self.cuadroI.setOutline(c.colorRedI)
		self.cuadroI.draw(self.win)
		# cantidad R
		self.cuadroR = g.Rectangle(c.pto0CuadroR,c.pto1CuadroR)
		self.cuadroR.setFill(c.colorGreenR)
		self.cuadroR.setOutline(c.colorGreenR)
		self.cuadroR.draw(self.win)
		# cantidad M
		self.cuadroM = g.Rectangle(c.pto0CuadroM,c.pto1CuadroM)
		self.cuadroM.setFill(c.colorWhiteM)
		self.cuadroM.setOutline('black')
		self.cuadroM.draw(self.win)
		# grupo grafica
		self.grafica1 = g.Rectangle(c.pto0Graf1,c.pto1Graf1)
		self.grafica1.setFill(c.colorGrayGraficas)
		self.grafica1.setOutline(c.colorFondo)
		self.grafica1.draw(self.win)
		self.ejeYG1 = g.Line(c.pto0EjeYG1,c.pto1EjeYG1)
		self.ejeYG1.setFill(c.colorLineas)
		self.ejeYG1.setWidth(2)
		self.ejeYG1.draw(self.win)
		self.ejeXG1 = g.Line(c.pto0EjeXG1,c.pto1EjeXG1)
		self.ejeXG1.setFill(c.colorLineas)
		self.ejeXG1.setWidth(2)
		self.ejeXG1.draw(self.win)
		self.grafica2 = g.Rectangle(c.pto0Graf2,c.pto1Graf2)
		self.grafica2.setFill(c.colorGrayGraficas)
		self.grafica2.setOutline(c.colorFondo)
		self.grafica2.draw(self.win)
		self.ejeYG1 = g.Line(c.pto0EjeYG2,c.pto1EjeYG2)
		self.ejeYG1.setFill(c.colorLineas)
		self.ejeYG1.setWidth(2)
		self.ejeYG1.draw(self.win)
		self.ejeXG2 = g.Line(c.pto0EjeXG2,c.pto1EjeXG2)
		self.ejeXG2.setFill(c.colorLineas)
		self.ejeXG2.setWidth(2)
		self.ejeXG2.draw(self.win)
		#simulacion
		self.simulacion = t.Tablero(self)

	def onClickIniciar(self):
		iniciar = 1
		centroBoton = self.botonIniciar.getCenter()
		centroBotonX = centroBoton.getX()
		centroBotonY = centroBoton.getY()
		while iniciar > 0:
			clicMouse = self.win.getMouse()
			clicMouseX = clicMouse.getX()
			clicMouseY = clicMouse.getY()
			if abs(centroBotonX - clicMouseX) < c.anchoBoton/2:
				if abs(centroBotonY - clicMouseY) < c.altoBoton/2:
					iniciar -= 1
					self.coefVirulencia = float(self.inputBoxAlfa.getText())
					self.coefRecuperacion = float(self.inputBoxBeta.getText())
					self.cantInfectados = int(self.inputCantMaxInfectados.getText())
					self.iteraciones = int(self.inputCantIteraciones.getText())
					self.cantDiasInfeccion = int(self.inputDuracionInfeccion.getText())
					self.botonIniciar.setFill(c.colorGreenBoton)
					self.etiquetaBoton.setText('INICIADA')
					self.etiquetaBoton.setFill('white')
					self.message.setTextColor(c.colorGreenBoton)
					self.message.setText('Seleccionar Infectados')
					# probabilidades
					self.infeccion = stats.rv_discrete(name="probabilidadInfectarse", values=([0,1],[self.coefVirulencia,1-self.coefVirulencia]))
					self.recuperacion = stats.rv_discrete(name="probabilidadRecuperarse", values=([2,3],[self.coefRecuperacion,1-self.coefRecuperacion]))
		self.simulacion.crearBloques()
		self.simulacion.setInfectados(self.cantInfectados, c.esc)		

	def onClickSalir(self):
		salir = 1
		centroBoton = self.botonIniciar.getCenter()
		centroBotonX = centroBoton.getX()
		centroBotonY = centroBoton.getY()
		while salir > 0:
			clicMouse = self.win.getMouse()
			clicMouseX = clicMouse.getX()
			clicMouseY = clicMouse.getY()
			if abs(centroBotonX - clicMouseX) < c.anchoBoton/2:
				if abs(centroBotonY - clicMouseY) < c.altoBoton/2:
					salir -= 1
					self.botonIniciar.setFill(c.colorRedI)
					self.etiquetaBoton.setFill(c.colorWhiteM)
		         
	
	def actualizarGraficas(self, cantidadS, cantidadI, cantidadR, cantidadM):
		altoejeY = abs(c.pto0EjeYG1.getY() - c.pto1EjeYG1.getY())
		escGraf1Y = ((altoejeY- c.tab*2)/(c.cantFilasColumnas*c.cantFilasColumnas))
		escGraf2Y = (altoejeY/(c.cantFilasColumnas*c.cantFilasColumnas))
		escGraf1X = round(abs(c.pto0EjeXG1.getX() - c.pto1EjeXG1.getX() + c.tab*2)/(self.iteraciones))
		puntoS = g.Point(c.pto0EjeXG1.getX()+(self.tic*escGraf1X),(c.pto1EjeYG1.getY()-cantidadS*escGraf1Y))
		circuloS = g.Circle(puntoS,c.tamPunto)
		circuloS.setOutline(c.colorBlueS)
		circuloS.setFill(c.colorBlueS)
		circuloS.draw(self.win)
		puntoR = g.Point(c.pto0EjeXG1.getX()+(self.tic*escGraf1X),(c.pto1EjeYG1.getY()-cantidadR*escGraf1Y))
		circuloR = g.Circle(puntoR,c.tamPunto)
		circuloR.setOutline(c.colorGreenR)
		circuloR.setFill(c.colorGreenR)
		circuloR.draw(self.win)
		puntoM = g.Point(c.pto0EjeXG1.getX()+(self.tic*escGraf1X),(c.pto1EjeYG1.getY()-cantidadM*escGraf1Y))
		circuloM = g.Circle(puntoM,c.tamPunto)
		circuloM.setOutline('black')
		circuloM.setFill(c.colorWhiteM)
		circuloM.draw(self.win)
		puntoI = g.Point(c.pto0EjeXG2.getX()+(self.tic*escGraf1X),(c.pto1EjeYG2.getY()-cantidadI*escGraf2Y))
		circuloI = g.Circle(puntoI,c.tamPunto)
		circuloI.setOutline(c.colorRedI)
		circuloI.setFill(c.colorRedI)
		circuloI.draw(self.win)


	def actualizarNotificaciones(self, cantidadS, cantidadI, cantidadR, cantidadM):
		self.etiquetaIteracion.setText('Iteracion n°: '+ str(self.tic))
		self.etiquetaS.setText('Susceptibles: '+ str(cantidadS))
		self.etiquetaI.setText('Infectados: '+ str(cantidadI))
		self.etiquetaR.setText('Recuperados: '+ str(cantidadR))
		self.etiquetaM.setText('Muertos: '+ str(cantidadM))
	

	def actualizarDatos(self, cantidadS, cantidadI, cantidadR, cantidadM):
		self.cantidadI = cantidadI
		self.actualizarNotificaciones(cantidadS, cantidadI, cantidadR, cantidadM)
		self.actualizarGraficas(cantidadS, cantidadI, cantidadR, cantidadM)


	def iniciarSimulacion(self):
		self.message.setTextColor(c.colorGreenBoton)
		self.message.setText('Simulación en Proceso')
		self.cantidadI = self.cantInfectados
		while self.iteraciones > self.tic and self.cantidadI > 0:
			self.tic += 1
			self.simulacion.simular(self.infeccion, self.recuperacion, self.cantDiasInfeccion)
		time.sleep(1)
		self.message.setTextColor(c.colorRedI)
		self.message.setText('Simulación Finalizada - Salir')
		self.botonIniciar.setFill(c.colorWhiteM)
		self.botonIniciar.setOutline(c.colorRedI)
		self.etiquetaBoton.setFill(c.colorRedI)
		self.etiquetaBoton.setText('SALIR')

