# -*- coding: utf-8 -*-

import graphics as g

cantFilasColumnas = 50

colorHeader = g.color_rgb(46, 64, 83)
colorFondo = g.color_rgb(192,192,192)
colorWhiteM = g.color_rgb( 255, 255, 255)
colorInput = g.color_rgb(240, 243, 244)
colorLineas = g.color_rgb(46, 64, 83)
colorGreenBoton = g.color_rgb( 34, 153, 84)
colorGrayGraficas = g.color_rgb(253, 254, 254)
colorBlueS = g.color_rgb(20, 34, 238)
colorRedI = g.color_rgb(255, 0, 0)
colorGreenR = g.color_rgb( 0, 255, 0)
altoVentana = 600
anchoVentana = 1200
tab = 10
altoH = 25
pto0Header = g.Point(0,0)
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
anchoS = altoI
altoS = altoI
esc = round(anchoS/cantFilasColumnas)
correccion = (anchoS - (esc*cantFilasColumnas))/2
pto0Sim = g.Point(pto0Notif.getX()+anchoN+tab+correccion,pto0Notif.getY()+correccion)
tamPunto = 3



