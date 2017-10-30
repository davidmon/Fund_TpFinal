# -*- coding: utf-8 -*-

import graphics as g
import random
import tablero as t
import time
import scipy
from scipy import stats


iteraciones = 100
cantInfectados = 1
cantidadS = 0
cantidadI = 0
cantidadR = 0
cantidadM = 0
coefEnferma  = 0.34 #enferma
coefRecupera = 0.6 #cura

#------------------------------------------------------------------------------------------------
# configuracion ventana
#------------------------------------------------------------------------------------------------
tamVentanaX = 930
tamVentanaY = 545
tabulacion = 10
colorInput = g.color_rgb(240, 243, 244)
colorHeader = g.color_rgb(46, 64, 83)
colorFondo = g.color_rgb(234, 236, 238)
colorBlueS = g.color_rgb(20, 34, 238)
colorRedI = g.color_rgb(255, 0, 0)
colorGreenR = g.color_rgb( 34, 153, 84)
colorWhiteM = g.color_rgb( 255, 255, 255)
colorLineas = g.color_rgb(46, 64, 83)

# dibuja tablero
win = g.GraphWin("FTI - TPFinal", tamVentanaX, tamVentanaY)
win.setBackground(colorFondo)

# header
tamHeaderY = 25
header = g.Rectangle(g.Point(0,0),g.Point(tamVentanaX,tamHeaderY))
header.setFill(colorHeader)
header.setOutline(colorHeader)
header.draw(win)
titulo = g.Text(g.Point(win.getWidth()/2, 13), 'Simulación Epidemia - Modelo SIR')
titulo.setTextColor('white')
titulo.setSize(11)
titulo.draw(win)

# grupo input
espacioY = 10
coorPX0 = espacioY
coorPY0 = espacioY+tamHeaderY
anchoI = 400 
altoI = 160
inputs = g.Rectangle(g.Point(coorPX0,coorPY0),g.Point(coorPX0+anchoI,coorPY0+altoI))
inputs.setFill('white')
inputs.setOutline(colorFondo)
inputs.draw(win)

# inputs - son 3
espacioBordeYI = 10
espacioYI = 60
coorTX = coorPX0 + anchoI/2  
coorTY = coorPY0 + espacioBordeYI+5
coorPIX1 = coorPX0 + anchoI/4  
coorPIY1 = coorPY0 + espacioYI + espacioBordeYI  
coorPIX2 = coorPX0 + anchoI/4 + anchoI/2   
coorPIY2 = coorPIY1 
anchoInput = 15
etiquetaTitulo = g.Text(g.Point(coorTX,coorTY), 'Ingresar valores de entrada')
etiquetaTitulo.setSize(12)
etiquetaTitulo.draw(win)
etiquetaInputBoxAlfa = g.Text(g.Point(coorPIX1,coorPIY1-tamHeaderY), 'Ingresar Valor de Alfa:')
etiquetaInputBoxAlfa.setSize(10)
etiquetaInputBoxAlfa.draw(win)
etiquetaInputBoxBeta = g.Text(g.Point(coorPIX1,coorPIY1+espacioYI-tamHeaderY), 'Ingresar Valor de Beta:')
etiquetaInputBoxBeta.setSize(10)
etiquetaInputBoxBeta.draw(win)
etiquetaInputBoxInfectados = g.Text(g.Point(coorPIX2,coorPIY1-tamHeaderY), 'Ingresar Cant Infectados:')
etiquetaInputBoxInfectados.setSize(10)
etiquetaInputBoxInfectados.draw(win)
etiquetaInputBoxIteraciones = g.Text(g.Point(coorPIX2,coorPIY1+espacioYI-tamHeaderY), 'Ingresar Cant Iteraciones:')
etiquetaInputBoxIteraciones.setSize(10)
etiquetaInputBoxIteraciones.draw(win)
inputBoxAlfa = g.Entry(g.Point(coorPIX1,coorPIY1), anchoInput)
inputBoxAlfa.setFill(colorInput)
inputBoxAlfa.setSize(11)
inputBoxAlfa.draw(win)
inputBoxAlfa.setText(coefEnferma)
inputBoxBeta = g.Entry(g.Point(coorPIX1,coorPIY1+espacioYI), anchoInput)
inputBoxBeta.setFill(colorInput)
inputBoxBeta.setSize(11)
inputBoxBeta.draw(win)
inputBoxBeta.setText(coefRecupera)
inputCantMaxInfectados = g.Entry(g.Point(coorPIX2,coorPIY1), anchoInput)
inputCantMaxInfectados.setFill(colorInput)
inputCantMaxInfectados.setSize(11)
inputCantMaxInfectados.draw(win)
inputCantMaxInfectados.setText(cantInfectados)
inputCantIteraciones = g.Entry(g.Point(coorPIX2,coorPIY1+espacioYI), anchoInput)
inputCantIteraciones.setFill(colorInput)
inputCantIteraciones.setSize(11)
inputCantIteraciones.draw(win)
inputCantIteraciones.setText(iteraciones)

# grupo simulacion
coorSI0 = espacioY + coorPX0 + anchoI
coorSY0 = coorPY0
anchoAltoS = 500 
simulación = g.Rectangle(g.Point(coorSI0,coorSY0),g.Point(coorSI0+anchoAltoS,coorSY0+anchoAltoS))
simulación.setFill('white')
simulación.draw(win)

# mensaje
coorMX0 = (coorPX0+anchoI)/2 
coorMY0 = coorPY0+altoI+tamHeaderY
message = g.Text(g.Point(coorMX0, coorMY0), 'Iniciar Simulación del Modelo')
message.setSize(12)
message.draw(win)

# iteraciones
coorMX0 = coorMX0
coorMY0 = coorMY0+tamHeaderY
etiquetaIteracion = g.Text(g.Point(coorMX0, coorMY0), 'Iteracion: -')
etiquetaIteracion.setSize(10)

# cantidad S
defasajeY = 15
coorSX = coorMX0
coorSY = coorMY0+defasajeY
etiquetaS = g.Text(g.Point(coorSX, coorSY), 'S: -')
etiquetaS.setSize(10)

# cantidad I
coorIX = coorMX0 
coorIY = coorMY0+defasajeY*2
etiquetaI = g.Text(g.Point(coorIX, coorIY), 'I: -')
etiquetaI.setSize(10)

# cantidad R
coorRX = coorMX0
coorRY = coorMY0+defasajeY*3
etiquetaR = g.Text(g.Point(coorRX, coorRY), 'R: -')
etiquetaR.setSize(10)

# cantidad M
coorMX = coorMX0
coorMY = coorMY0+defasajeY*4
etiquetaM = g.Text(g.Point(coorMX, coorMY), 'M: -')
etiquetaM.setSize(10)


# grupo grafica
coorGX0 = espacioY
coorGY0 = espacioY+tamHeaderY+coorMY
grafica = g.Rectangle(g.Point(coorGX0,coorGY0),g.Point(coorGX0+anchoI,coorGY0+altoI))
grafica.setFill('white')
grafica.setOutline(colorFondo)
grafica.draw(win)
 

ejeY = g.Line(g.Point(espacioY*2,coorGY0+10),g.Point(espacioY*2,coorGY0+altoI-10))
ejeY.setFill(colorLineas)
ejeY.draw(win)
ejeX = g.Line(g.Point(espacioY*2,coorGY0+altoI-10),g.Point(espacioY*2+anchoI-20,coorGY0+altoI-10))
ejeX.setFill(colorLineas)
ejeX.draw(win)

# boton aceptar
anchoBoton = 120 
altoBoton = 25
coorBX0 = coorMX0 - anchoBoton/2
coorBY0 = 510
botonIniciar = g.Rectangle(g.Point(coorBX0,coorBY0), g.Point(coorBX0+anchoBoton,coorBY0+altoBoton))
botonIniciar.setFill('white')
botonIniciar.setOutline(colorGreenR)
botonIniciar.setWidth(2)
botonIniciar.draw(win)
etiquetaBoton = g.Text(g.Point(coorMX0, coorBY0-2+altoBoton/2), 'INICIAR')
etiquetaBoton.setSize(10)
etiquetaBoton.setFill(colorGreenR)
etiquetaBoton.draw(win)

#------------------------------------------------------------------------------------------------
# configuracion simulacion
#------------------------------------------------------------------------------------------------

cantFilasColumnas = 50
tic = 0
blocks = []
vecinosI = 0
duracionInfeccion = 0
scale = round(anchoAltoS/cantFilasColumnas)

for x in range(scale, anchoAltoS +1, scale):
    for y in range(scale, anchoAltoS +1, scale):
        point1 = g.Point(x + coorSI0, y + coorSY0)
        point2 = g.Point(x + coorSI0 - scale, y + coorSY0 - scale)
        celda = g.Rectangle(point1, point2)
        celda.setFill(colorBlueS)
        block = [celda, "suceptible", vecinosI, "suceptible", duracionInfeccion]
        block[0].draw(win)
        blocks.append(block)

#------------------------------------------------------------------------------------------------
# simulacion
#------------------------------------------------------------------------------------------------

iniciar = 1
while iniciar > 0:
    clicMouse = win.getMouse()
    clicMouseX = clicMouse.getX()
    clicMouseY = clicMouse.getY()
    centroBoton = botonIniciar.getCenter()
    centroBotonX = centroBoton.getX()
    centroBotonY = centroBoton.getY()
    if abs(centroBotonX - clicMouseX) < anchoBoton/2:
        if abs(centroBotonY - clicMouseY) < altoBoton/2:
            iniciar -= 1
            coefEnferma = float(inputBoxAlfa.getText())
            coefRecupera = float(inputBoxBeta.getText())
            cantInfectados = int(inputCantMaxInfectados.getText())
            iteraciones = int(inputCantIteraciones.getText())
            botonIniciar.setFill(colorGreenR)
            etiquetaBoton.setText('INICIADA')
            etiquetaBoton.setFill('white')
            message.setTextColor(colorGreenR)
            message.setText('Seleccionar Infectados')

while cantInfectados > 0:
    mouse = win.getMouse()
    mouse_x = mouse.getX()
    mouse_y = mouse.getY()
    for index in range(0, len(blocks)):
        center = blocks[index][0].getCenter()
        center_x = center.getX()
        center_y = center.getY()
        if abs(center_x - mouse_x) < scale/2:
            if abs(center_y - mouse_y) < scale/2:
                blocks[index][0].setFill(colorRedI)
                blocks[index][1] = "infectada"
                cantInfectados -= 1

# anexa las celdas vecinas a cada bloque
t.indexing(blocks, cantFilasColumnas)

message.setTextColor(colorGreenR)
message.setText('Simulación en Proceso')
etiquetaIteracion.draw(win)
etiquetaS.draw(win)
etiquetaI.draw(win)
etiquetaR.draw(win)
etiquetaM.draw(win)

infeccion = stats.rv_discrete(name="probabilidadInfectarse", values=([0,1],[coefEnferma,1-coefEnferma]))
recuperacion = stats.rv_discrete(name="probabilidadRecuperarse", values=([2,3],[coefRecupera,1-coefRecupera]))

while iteraciones > tic:
    cantidadS = len(blocks)
    for index in range(0, len(blocks)):
        #reglas
        if blocks[index][1] == "suceptible":
            for x in blocks[index][5]:
                if blocks[x][1] == "infectada":
                    blocks[index][2] += 1
            if blocks[index][2] >= 1:


                #falta mucho vecinos
                

                if infeccion.rvs() == 0:    
                    blocks[index][3] = "infectada"
                    cantidadS -= 1
                    cantidadI += 1 
                #else:
                #    blocks[index][3] = "suceptible"

        blocks[index][2] = 0     
        if blocks[index][1] == "infectada":
            if blocks[index][4] != 2: # definir variable 10
                blocks[index][4] += 1 
                if recuperacion.rvs() == 2:
                    blocks[index][3] = "recuperada"
                    cantidadR += 1
                    cantidadI -= 1
                #else:
                #    blocks[index][3] = "infectada"
            else:
                blocks[index][3] = "muerta"
                cantidadM += 1
                cantidadI -= 1
    # ahora dibuja
    for index in range(0, len(blocks)):
        blocks[index][2] = 0
        if blocks[index][3] == "suceptible":
            blocks[index][1] = "suceptible"
            blocks[index][0].setFill(colorBlueS)
        if blocks[index][3] == "infectada":
            blocks[index][1] = "infectada"
            blocks[index][0].setFill(colorRedI)
        if blocks[index][3] == "muerta":
            blocks[index][1] = "muerta"
            blocks[index][0].setFill(colorWhiteM)    
        if blocks[index][3] == "recuperada":
            blocks[index][1] = "recuperada"
            blocks[index][0].setFill(colorGreenR)    
    tic += 1
    etiquetaIteracion.setText('Iteracion: '+ str(tic))
    etiquetaS.setText('S: '+ str(cantidadS))
    etiquetaI.setText('I: '+ str(cantidadI))
    etiquetaR.setText('R: '+ str(cantidadR))
    etiquetaM.setText('M: '+ str(cantidadM))
    time.sleep(0.5)

time.sleep(1)
message.setTextColor(colorRedI)
message.setText('Simulación Finalizada - Salir')
botonIniciar.setFill('white')
botonIniciar.setOutline(colorRedI)
etiquetaBoton.setFill(colorRedI)
etiquetaBoton.setText('SALIR')

salir = 1
while salir > 0:
    clicMouse = win.getMouse()
    clicMouseX = clicMouse.getX()
    clicMouseY = clicMouse.getY()
    centroBoton = botonIniciar.getCenter()
    centroBotonX = centroBoton.getX()
    centroBotonY = centroBoton.getY()
    if abs(centroBotonX - clicMouseX) < anchoBoton/2:
        if abs(centroBotonY - clicMouseY) < altoBoton/2:
            salir -= 1
            botonIniciar.setFill(colorRedI)
            etiquetaBoton.setFill('white')
            win.close()