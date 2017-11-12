# -*- coding: utf-8 -*-


import ventana as v
import configuracion as c

def main():
    ventana = v.Ventana()
    ventana.graficar()
    ventana.simulacion.dibujarse()
    ventana.onClickIniciar()
    ventana.iniciarSimulacion()
    ventana.onClickSalir()
    ventana.win.close()


if __name__ == '__main__':
    main()
