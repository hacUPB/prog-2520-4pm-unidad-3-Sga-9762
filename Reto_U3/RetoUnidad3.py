# Ejercicios Reto Unidad 3

from modulo import *



choice = int(input("**¡Bienvenido!** Escoja una de las opciones a continuación:\n1. Simulador de Ascenso y Control de Vuelo\n2. Simulador de Gestión del Centro de Gravedad\n3. Sistema de Alerta de Velocidad\n4. Salir\n SU SELECCION: "))

while True:
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            SpdAlert()
        case 4:
            break
        case _:
            pass


