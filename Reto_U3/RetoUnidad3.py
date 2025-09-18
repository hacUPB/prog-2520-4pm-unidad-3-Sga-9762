# Ejercicios Reto Unidad 3

from modulo import *





while True:
    choice = int(input("**¡Bienvenido!** Escoja una de las opciones a continuación:\n1. Simulador de Ascenso y Control de Vuelo\n2. Simulador de Gestión del Centro de Gravedad\n3. Sistema de Alerta de Velocidad\n4. Salir\n SU SELECCION: "))
    match choice:
        case 1:
            altitud_crucero = int(input("¡Bienvenido al simulador de presurización y ascenso de vuelo!\n Introduzca la altitud de crucero del vuelo: "))
            Ascenso(altitud_crucero)
        case 2:
            fuelsim()
        case 3:
            SpdAlert()
        case 4:
            break
        case _:
            print("**La opción seleccionada no es válida**")


