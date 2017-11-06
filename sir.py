# -*- coding: utf-8 -*-

import graphics as g
import random
import tablero as t
import time
import scipy
from scipy import stats


iteraciones = 40
cantInfectados = 5
cantidadS = 0
cantidadI = 0
cantidadR = 0
cantidadM = 0
coefVirulencia = 0.34
coefRecuperacion = 0.6
cantFilasColumnas = 50
tic = 0
blocks = []
vecinosI = 0
cantDiasInfectado = 0
cantDiasInfeccion = 3
valGraf = []


#------------------------------------------------------------------------------------------------
# configuracion ventana
#------------------------------------------------------------------------------------------------

# colores
colorInput = g.color_rgb(240, 243, 244)
colorHeader = g.color_rgb(46, 64, 83)
colorFondo = g.color_rgb(192,192,192)
colorBlueS = g.color_rgb(20, 34, 238)
colorRedI = g.color_rgb(255, 0, 0)
colorGreenR = g.color_rgb( 0, 255, 0)
colorWhiteM = g.color_rgb( 255, 255, 255)
colorLineas = g.color_rgb(46, 64, 83)
colorGreenBoton = g.color_rgb( 34, 153, 84)
colorGrayGraficas = g.color_rgb(253, 254, 254)
# conf medidas
tab = 10
altoVentana = 600
anchoVentana = 1200
pto0Header = g.Point(0,0)
altoH = 25
anchoH = anchoVentana
pto0Input = g.Point(tab,tab+altoH)  
altoI = altoVentana - altoH - tab*2
anchoI = int((anchoVentana - (altoI + tab*3))/4)
pto0LInput = g.Point(int(tab+anchoI/2),int(pto0Input.getY()+tab+tab/2))
anchoInput = 18 
separacionInput = 55
ptOInputBoxAlfa = g.Point(pto0LInput.getX(),pto0LInput.getY()+separacionInput)
ptOInputBoxBeta = g.Point(pto0LInput.getX(),ptOInputBoxAlfa.getY()+separacionInput)
ptODurInfeccion = g.Point(pto0LInput.getX(),ptOInputBoxBeta.getY()+separacionInput)
ptOInputCantIteraciones = g.Point(pto0LInput.getX(),ptODurInfeccion.getY()+separacionInput)
ptOInputCantFilas = g.Point(pto0LInput.getX(),ptOInputCantIteraciones.getY()+separacionInput)
ptOInputCantMaxInfectados = g.Point(pto0LInput.getX(),ptOInputCantFilas.getY()+separacionInput)
defasajeLInput = 25
ptOLInputBoxAlfa = g.Point(pto0LInput.getX(),ptOInputBoxAlfa.getY()-defasajeLInput)
ptOLInputBoxBeta = g.Point(pto0LInput.getX(),ptOInputBoxBeta.getY()-defasajeLInput)
ptOLInputDiasInF = g.Point(pto0LInput.getX(),ptODurInfeccion.getY()-defasajeLInput)
ptOLInputCantIteraciones = g.Point(pto0LInput.getX(),ptOInputCantIteraciones.getY()-defasajeLInput)
ptOLInputCantFilas = g.Point(pto0LInput.getX(),ptOInputCantFilas.getY()-defasajeLInput)
ptOLInputCantMaxInfectados = g.Point(pto0LInput.getX(),ptOInputCantMaxInfectados.getY()-defasajeLInput)
pto0Notif = g.Point(pto0Input.getX()+anchoI+tab,pto0Input.getY())  
altoN = altoI
anchoN = anchoVentana - anchoI - tab*4 - altoI
altoBoton = 25
pto0Boton = g.Point(pto0Input.getX()+anchoI-tab,pto0Input.getY()+altoI-tab-altoBoton)
pto1Boton = g.Point(pto0Input.getX()+tab,pto0Input.getY()+altoI-tab)
anchoBoton = pto0Boton.getX()-pto1Boton.getX()
pto0LBoton = g.Point(int(pto0Boton.getX()-anchoBoton/2),int(pto0Boton.getY()+altoBoton/2))
pto0Mensaje = g.Point(pto0Notif.getX()+int(anchoN/2),pto0Input.getY()+tab*2)
defasajeNotif = 18
pto0NotifIt = g.Point(pto0Mensaje.getX(),pto0Mensaje.getY()+defasajeNotif)
pto0NotifS = g.Point(pto0NotifIt.getX(),pto0NotifIt.getY()+defasajeNotif)
pto0NotifI = g.Point(pto0NotifIt.getX(),pto0NotifS.getY()+defasajeNotif)
pto0NotifR = g.Point(pto0NotifIt.getX(),pto0NotifI.getY()+defasajeNotif)
pto0NotifM = g.Point(pto0NotifIt.getX(),pto0NotifR.getY()+defasajeNotif)
anchoS = altoI
altoS = altoI
esc = round(anchoS/cantFilasColumnas)
correccion = (anchoS - (esc*cantFilasColumnas))/2
pto0Sim = g.Point(pto0Notif.getX()+anchoN+tab+correccion,pto0Notif.getY()+correccion)
pto0Graf1 = g.Point(pto0Notif.getX()+tab, pto0NotifM.getY()+tab*2)
altoGraf = (altoVentana - pto0Graf1.getX() - tab*2)/2
pto1Graf1 = g.Point(pto0Notif.getX()+anchoN-tab,pto0Graf1.getY()+altoGraf)
pto0Graf2 = g.Point(pto0Notif.getX()+tab, pto1Graf1.getY()+tab)
pto1Graf2 = g.Point(pto0Notif.getX()+anchoN-tab,pto0Graf2.getY()+altoGraf)
pto0EjeYG1 = g.Point(pto0Graf1.getX()+tab,pto0Graf1.getY()+tab)
pto1EjeYG1 = g.Point(pto0Graf1.getX()+tab,pto0Graf1.getY()+altoGraf-tab)
pto0EjeXG1 = g.Point(pto0Graf1.getX()+tab,pto1Graf1.getY()-tab)
pto1EjeXG1 = g.Point(pto1Graf1.getX()-tab,pto1Graf1.getY()-tab)
pto0EjeYG2 = g.Point(pto0Graf2.getX()+tab,pto0Graf2.getY()+tab)
pto1EjeYG2 = g.Point(pto0Graf2.getX()+tab,pto0Graf2.getY()+altoGraf-tab)
pto0EjeXG2 = g.Point(pto0Graf2.getX()+tab,pto1Graf2.getY()-tab)
pto1EjeXG2 = g.Point(pto1Graf2.getX()-tab,pto1Graf2.getY()-tab)
pto0CuadroS = g.Point(pto0NotifS.getX()-65,pto0NotifS.getY()-5)
pto1CuadroS = g.Point(pto0NotifS.getX()-75,pto0NotifS.getY()+5)
pto0CuadroI = g.Point(pto0NotifI.getX()-65,pto0NotifI.getY()-5)
pto1CuadroI = g.Point(pto0NotifI.getX()-75,pto0NotifI.getY()+5)
pto0CuadroR = g.Point(pto0NotifR.getX()-65,pto0NotifR.getY()-5)
pto1CuadroR = g.Point(pto0NotifR.getX()-75,pto0NotifR.getY()+5)
pto0CuadroM = g.Point(pto0NotifM.getX()-65,pto0NotifM.getY()-5)
pto1CuadroM = g.Point(pto0NotifM.getX()-75,pto0NotifM.getY()+5)
# tablero
win = g.GraphWin("FTI - TPFinal", anchoVentana, altoVentana)
win.setBackground(colorFondo)
# header
header = g.Rectangle(pto0Header,g.Point(pto0Header.getX()+anchoH,pto0Header.getY()+altoH))
header.setFill(colorHeader)
header.setOutline(colorHeader)
header.draw(win)
titulo = g.Text(g.Point(win.getWidth()/2, 13), 'Simulación Epidemia - Modelo SIR')
titulo.setTextColor('white')
titulo.setSize(11)
titulo.draw(win)
# grupo inputs
inputs = g.Rectangle(pto0Input,g.Point(pto0Input.getX()+anchoI,pto0Input.getY()+altoI))
inputs.setFill(colorWhiteM)
inputs.setOutline(colorFondo)
inputs.draw(win)
# titulo inputs
labelInput = g.Text(pto0LInput, 'VALORES DE ENTRADA')
labelInput.setSize(9)
labelInput.draw(win)
#inputs
inputBoxAlfa = g.Entry(ptOInputBoxAlfa, anchoInput)
inputBoxAlfa.setFill(colorInput)
inputBoxAlfa.setSize(10)
inputBoxAlfa.draw(win)
inputBoxAlfa.setText(coefVirulencia)
inputBoxBeta = g.Entry(ptOInputBoxBeta, anchoInput)
inputBoxBeta.setFill(colorInput)
inputBoxBeta.setSize(10)
inputBoxBeta.draw(win)
inputBoxBeta.setText(coefRecuperacion)
inputDuracionInfeccion = g.Entry(ptODurInfeccion, anchoInput)
inputDuracionInfeccion.setFill(colorInput)
inputDuracionInfeccion.setSize(10)
inputDuracionInfeccion.draw(win)
inputDuracionInfeccion.setText(cantDiasInfeccion)
inputCantIteraciones = g.Entry(ptOInputCantIteraciones, anchoInput)
inputCantIteraciones.setFill(colorInput)
inputCantIteraciones.setSize(10)
inputCantIteraciones.draw(win)
inputCantIteraciones.setText(iteraciones)
inputCantFilas = g.Entry(ptOInputCantFilas, anchoInput)
inputCantFilas.setFill(colorInput)
inputCantFilas.setSize(10)
inputCantFilas.draw(win)
inputCantFilas.setText(cantFilasColumnas)
inputCantMaxInfectados = g.Entry(ptOInputCantMaxInfectados, anchoInput)
inputCantMaxInfectados.setFill(colorInput)
inputCantMaxInfectados.setSize(10)
inputCantMaxInfectados.draw(win)
inputCantMaxInfectados.setText(cantInfectados)
# label inputs
etiquetaInputBoxAlfa = g.Text(ptOLInputBoxAlfa,'Coef Virulencia:')
etiquetaInputBoxAlfa.setSize(10)
etiquetaInputBoxAlfa.draw(win)
etiquetaInputBoxBeta = g.Text(ptOLInputBoxBeta,'Coef Recuperación:')
etiquetaInputBoxBeta.setSize(10)
etiquetaInputBoxBeta.draw(win)
etiquetaInputBoxDInf = g.Text(ptOLInputDiasInF,'Duración Infección:')
etiquetaInputBoxDInf.setSize(10)
etiquetaInputBoxDInf.draw(win)
etiquetaInputBoxIteraciones = g.Text(ptOLInputCantIteraciones,'Cant Iteraciones:')
etiquetaInputBoxIteraciones.setSize(10)
etiquetaInputBoxIteraciones.draw(win)
etiquetaInputBoxFilas = g.Text(ptOLInputCantFilas,'Cant Filas:')
etiquetaInputBoxFilas.setSize(10)
etiquetaInputBoxFilas.draw(win)
etiquetaInputBoxInfectados = g.Text(ptOLInputCantMaxInfectados,'Cant Infectados:')
etiquetaInputBoxInfectados.setSize(10)
etiquetaInputBoxInfectados.draw(win)
# grupo notificacion
grafica = g.Rectangle(pto0Notif,g.Point(pto0Notif.getX()+anchoN,pto0Notif.getY()+altoN))
grafica.setFill(colorWhiteM)
grafica.setOutline(colorFondo)
grafica.draw(win)
# boton aceptar
botonIniciar = g.Rectangle(pto0Boton,pto1Boton)
botonIniciar.setFill(colorWhiteM)
botonIniciar.setOutline(colorGreenBoton)
botonIniciar.setWidth(2)
botonIniciar.draw(win)
etiquetaBoton = g.Text(pto0LBoton, 'INICIAR')
etiquetaBoton.setSize(10)
etiquetaBoton.setFill(colorGreenBoton)
etiquetaBoton.draw(win)
# mensaje
message = g.Text(pto0Mensaje,'Iniciar Simulación del Modelo')
message.setSize(12)
message.draw(win)
# iteraciones
etiquetaIteracion = g.Text(pto0NotifIt,'Iteracion n°: -')
etiquetaIteracion.setSize(10)
etiquetaIteracion.draw(win)
# cantidad S
etiquetaS = g.Text(pto0NotifS,'Susceptibles: -')
etiquetaS.setSize(10)
etiquetaS.draw(win)
# cantidad I
etiquetaI = g.Text(pto0NotifI, 'Infectados: -')
etiquetaI.setSize(10)
etiquetaI.draw(win)
# cantidad R
etiquetaR = g.Text(pto0NotifR, 'Recuperados: -')
etiquetaR.setSize(10)
etiquetaR.draw(win)
# cantidad M
etiquetaM = g.Text(pto0NotifM, 'Muertos: -')
etiquetaM.setSize(10)
etiquetaM.draw(win)
# id cantidad S
cuadroS = g.Rectangle(pto0CuadroS,pto1CuadroS)
cuadroS.setFill(colorBlueS)
cuadroS.setOutline(colorBlueS)
cuadroS.draw(win)
# id cantidad I
cuadroI = g.Rectangle(pto0CuadroI,pto1CuadroI)
cuadroI.setFill(colorRedI)
cuadroI.setOutline(colorRedI)
cuadroI.draw(win)
# cantidad R
cuadroR = g.Rectangle(pto0CuadroR,pto1CuadroR)
cuadroR.setFill(colorGreenR)
cuadroR.setOutline(colorGreenR)
cuadroR.draw(win)
# cantidad M
cuadroM = g.Rectangle(pto0CuadroM,pto1CuadroM)
cuadroM.setFill(colorWhiteM)
cuadroM.setOutline('black')
cuadroM.draw(win)
# grupo grafica
grafica1 = g.Rectangle(pto0Graf1,pto1Graf1)
grafica1.setFill(colorGrayGraficas)
grafica1.setOutline(colorFondo)
grafica1.draw(win)
ejeYG1 = g.Line(pto0EjeYG1,pto1EjeYG1)
ejeYG1.setFill(colorLineas)
ejeYG1.setWidth(2)
ejeYG1.draw(win)
ejeXG1 = g.Line(pto0EjeXG1,pto1EjeXG1)
ejeXG1.setFill(colorLineas)
ejeXG1.setWidth(2)
ejeXG1.draw(win)
grafica2 = g.Rectangle(pto0Graf2,pto1Graf2)
grafica2.setFill(colorGrayGraficas)
grafica2.setOutline(colorFondo)
grafica2.draw(win)
ejeYG1 = g.Line(pto0EjeYG2,pto1EjeYG2)
ejeYG1.setFill(colorLineas)
ejeYG1.setWidth(2)
ejeYG1.draw(win)
ejeXG2 = g.Line(pto0EjeXG2,pto1EjeXG2)
ejeXG2.setFill(colorLineas)
ejeXG2.setWidth(2)
ejeXG2.draw(win)
#simulacion
simulacion = g.Rectangle(pto0Sim, g.Point(pto0Sim.getX()+anchoS-5,pto0Sim.getY()+anchoS-5))
simulacion.setFill(colorBlueS)
simulacion.setOutline(colorBlueS)
simulacion.draw(win)

#------------------------------------------------------------------------------------------------
# boton aceptar
#------------------------------------------------------------------------------------------------
iniciar = 1
centroBoton = botonIniciar.getCenter()
centroBotonX = centroBoton.getX()
centroBotonY = centroBoton.getY()
while iniciar > 0:
    clicMouse = win.getMouse()
    clicMouseX = clicMouse.getX()
    clicMouseY = clicMouse.getY()
    if abs(centroBotonX - clicMouseX) < anchoBoton/2:
        if abs(centroBotonY - clicMouseY) < altoBoton/2:
            iniciar -= 1
            coefVirulencia = float(inputBoxAlfa.getText())
            coefRecuperacion = float(inputBoxBeta.getText())
            cantInfectados = int(inputCantMaxInfectados.getText())
            iteraciones = int(inputCantIteraciones.getText())
            cantFilasColumnas = int(inputCantFilas.getText())
            cantDiasInfeccion = int(inputDuracionInfeccion.getText())
            botonIniciar.setFill(colorGreenBoton)
            etiquetaBoton.setText('INICIADA')
            etiquetaBoton.setFill('white')
            message.setTextColor(colorGreenBoton)
            message.setText('Seleccionar Infectados')

#------------------------------------------------------------------------------------------------
# configuracion simulacion
#------------------------------------------------------------------------------------------------
esc = round(anchoS/cantFilasColumnas)
for x in range(esc, anchoS +1, esc):
    for y in range(esc, anchoS +1, esc):
        point1 = g.Point(x+pto0Sim.getX(), y+pto0Sim.getY())
        point2 = g.Point(x+pto0Sim.getX()-esc, y+pto0Sim.getY()-esc)
        celda = g.Rectangle(point1, point2)
        celda.setFill(colorBlueS)
        block = [celda, "susceptible", vecinosI, "susceptible", cantDiasInfectado]
        block[0].draw(win)
        blocks.append(block)
simulacion.setFill(colorFondo)
simulacion.setOutline(colorFondo)

#------------------------------------------------------------------------------------------------
# simulacion
#------------------------------------------------------------------------------------------------
while cantInfectados > 0:
    mouse = win.getMouse()
    mouse_x = mouse.getX()
    mouse_y = mouse.getY()
    for index in range(0, len(blocks)):
        center = blocks[index][0].getCenter()
        center_x = center.getX()
        center_y = center.getY()
        if abs(center_x - mouse_x) < esc/2:
            if abs(center_y - mouse_y) < esc/2:
                blocks[index][0].setFill(colorRedI)
                blocks[index][1] = "infectada"
                cantInfectados -= 1
# anexa las celdas vecinas a cada bloque
t.indexing(blocks, cantFilasColumnas)
time.sleep(0.5)
message.setTextColor(colorGreenBoton)
message.setText('Simulación en Proceso')
cantidadS = len(blocks)
cantidadI = int(inputCantMaxInfectados.getText())
cantidadS -= cantidadI 
infeccion = stats.rv_discrete(name="probabilidadInfectarse", values=([0,1],[coefVirulencia,1-coefVirulencia]))
recuperacion = stats.rv_discrete(name="probabilidadRecuperarse", values=([2,3],[coefRecuperacion,1-coefRecuperacion]))
altoejeY = abs(pto0EjeYG1.getY() - pto1EjeYG1.getY())
escGraf1Y = ((altoejeY- tab*2)/(cantFilasColumnas*cantFilasColumnas))
escGraf2Y = (altoejeY/(cantFilasColumnas*cantFilasColumnas))
escGraf1X = round(abs(pto0EjeXG1.getX() - pto1EjeXG1.getX() + tab*2)/(iteraciones))

while iteraciones > tic and cantidadI > 0:
    for index in range(0, len(blocks)):
        #reglas
        if blocks[index][1] == "susceptible":
            for x in blocks[index][5]:
                if blocks[x][1] == "infectada":
                    blocks[index][2] += 1
            if blocks[index][2] >= 1:
                for inf in range (0,blocks[index][2]):
                    if blocks[index][3] == "susceptible":    
                        if infeccion.rvs() == 0:    
                            blocks[index][3] = "infectada"
                            cantidadS -= 1
                            cantidadI += 1 
                        else:
                            blocks[index][3] = "susceptible"
        blocks[index][2] = 0
        if blocks[index][1] == "infectada":
            if blocks[index][4] <= cantDiasInfeccion: 
                blocks[index][4] += 1 
                if recuperacion.rvs() == 2:
                    blocks[index][3] = "recuperada"
                    cantidadR += 1
                    cantidadI -= 1
                else:
                    blocks[index][3] = "infectada"
            else:
                blocks[index][3] = "muerta"
                cantidadM += 1
                cantidadI -= 1
    # dibuja y actualiza estados
    for index in range(0, len(blocks)):
        blocks[index][2] = 0
        if blocks[index][3] == "susceptible":
            blocks[index][1] = "susceptible"
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
    valores = [tic,cantidadS,cantidadI,cantidadR,cantidadM]
    valGraf.append(valores)
    # actualiza notificaciones
    etiquetaIteracion.setText('Iteracion n°: '+ str(tic))
    etiquetaS.setText('Susceptibles: '+ str(cantidadS))
    etiquetaI.setText('Infectados: '+ str(cantidadI))
    etiquetaR.setText('Recuperados: '+ str(cantidadR))
    etiquetaM.setText('Muertos: '+ str(cantidadM))
    puntoS = g.Point(pto0EjeXG1.getX()+(tic*escGraf1X),(pto1EjeYG1.getY()-cantidadS*escGraf1Y))
    circuloS = g.Circle(puntoS,3)
    circuloS.setOutline(colorBlueS)
    circuloS.setFill(colorBlueS)
    circuloS.draw(win)
    puntoR = g.Point(pto0EjeXG1.getX()+(tic*escGraf1X),(pto1EjeYG1.getY()-cantidadR*escGraf1Y))
    circuloR = g.Circle(puntoR,3)
    circuloR.setOutline(colorGreenR)
    circuloR.setFill(colorGreenR)
    circuloR.draw(win)
    puntoM = g.Point(pto0EjeXG1.getX()+(tic*escGraf1X),(pto1EjeYG1.getY()-cantidadM*escGraf1Y))
    circuloM = g.Circle(puntoM,3)
    circuloM.setOutline('black')
    circuloM.setFill(colorWhiteM)
    circuloM.draw(win)
    puntoI = g.Point(pto0EjeXG2.getX()+(tic*escGraf1X),(pto1EjeYG2.getY()-cantidadI*escGraf2Y))
    circuloI = g.Circle(puntoI,3)
    circuloI.setOutline(colorRedI)
    circuloI.setFill(colorRedI)
    circuloI.draw(win)

#------------------------------------------------------------------------------------------------
# boton salir
#------------------------------------------------------------------------------------------------
time.sleep(1)
message.setTextColor(colorRedI)
message.setText('Simulación Finalizada - Salir')
botonIniciar.setFill(colorWhiteM)
botonIniciar.setOutline(colorRedI)
etiquetaBoton.setFill(colorRedI)
etiquetaBoton.setText('SALIR')

salir = 1
centroBoton = botonIniciar.getCenter()
centroBotonX = centroBoton.getX()
centroBotonY = centroBoton.getY()
while salir > 0:
    clicMouse = win.getMouse()
    clicMouseX = clicMouse.getX()
    clicMouseY = clicMouse.getY()
    if abs(centroBotonX - clicMouseX) < anchoBoton/2:
        if abs(centroBotonY - clicMouseY) < altoBoton/2:
            salir -= 1
            botonIniciar.setFill(colorRedI)
            etiquetaBoton.setFill(colorWhiteM)
            win.close()