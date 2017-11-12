# -*- coding: utf-8 -*-

import graphics as g
import bloque as b
import configuracion as c


class Tablero():

    def __init__(self, ventana):
        self.bloques = []
        self.ventana = ventana
        self.cantidadS = 0
        self.cantidadI = 0
        self.cantidadR = 0
        self.cantidadM = 0
        

    def dibujarse(self):
        self.simulacion = g.Rectangle(c.pto0Sim, g.Point(c.pto0Sim.getX()+c.anchoS-5,c.pto0Sim.getY()+c.anchoS-5))
        self.simulacion.setFill(c.colorBlueS)
        self.simulacion.setOutline(c.colorBlueS)
        self.simulacion.draw(self.ventana.win)


    def crearBloques(self):
        self.cantidadS = c.cantFilasColumnas*c.cantFilasColumnas
        esc = round(c.anchoS/c.cantFilasColumnas)
        for x in range(esc, c.anchoS+1, esc):
            for y in range(esc, c.altoS+1, esc):
                point1 = g.Point(x+c.pto0Sim.getX(), y+c.pto0Sim.getY())
                point2 = g.Point(x+c.pto0Sim.getX()-esc, y+c.pto0Sim.getY()-esc)
                celda = g.Rectangle(point1, point2)
                celda.setFill(c.colorBlueS)
                bloque = b.Bloque(self, celda)
                bloque.celda.draw(self.ventana.win)
                self.bloques.append(bloque)
        self.ocultarse()


    def ocultarse(self):
        self.simulacion.undraw()


    def setInfectados(self, cantInfectados, esc):
        self.cantidadS -= cantInfectados
        self.cantidadI = cantInfectados
        cantInfectados = cantInfectados
        while cantInfectados > 0:    
            mouse = self.ventana.win.getMouse()
            mouse_x = mouse.getX()
            mouse_y = mouse.getY()
            for index in range(0, len(self.bloques)):
                center = self.bloques[index].celda.getCenter()
                center_x = center.getX()
                center_y = center.getY()
                if abs(center_x - mouse_x) < esc/2:
                    if abs(center_y - mouse_y) < esc/2:
                        self.bloques[index].celda.setFill(c.colorRedI)
                        self.bloques[index].estadoactual = "infectada"
                        cantInfectados -= 1
        self.anexarVecinos()


    def anexarVecinos(self):
        check = []
        objects = len(self.bloques)
        for index in range(0, objects):
            step = index - c.cantFilasColumnas -1
            for num in range(0, 3):
                count = 0
                while count < 3:
                    current = count + step
                    if current != index and current >= 0 and current < objects:
                        check.append(current)
                    count += 1
                step += c.cantFilasColumnas
            self.cleaning(self.bloques, c.cantFilasColumnas, check, index)
            check = []


    def cleaning(self, blocks, squares_x, check, index):
        if (index % squares_x) == 0:
            num = len(check)
            while num > 0:
                num -= 1
                if (check[num] +1) % squares_x == 0 :
                    del(check[num])
        elif ((index +1) % squares_x) == 0:
            num = len(check)
            while num > 0:
                num -= 1
                if (check[num]) % squares_x == 0 :
                    del(check[num])
        self.bloques[index].vecinos = check
        check = []

    
    def retornarVecino(self, vecino):
        return self.bloques[vecino]


    def simular(self, infeccion, recuperacion, cantDiasInfeccion):
        for index in range(0, len(self.bloques)):
            self.bloques[index].evaluate(infeccion, recuperacion, cantDiasInfeccion)
        for index in range(0, len(self.bloques)):
            self.bloques[index].actualizate()
        self.ventana.actualizarDatos(self.cantidadS, self.cantidadI, self.cantidadR, self.cantidadM)