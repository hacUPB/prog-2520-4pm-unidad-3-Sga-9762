'''
def suma(a, b):
	resultado = a + b
	return resultado


#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)
'''
'''
# Ejercicio 1
import random
j = 0
def tabla_multi(num):
    for i in range(1, 11):
        result = num*i
        print(f"{num} x {i} = {result}")
 
numero = int(input("Ingrese un número entero: "))
tabla_multi(numero)
'''

# Ejercicio 2 
'''
Función: menú
Parámetros de entrada: ninguno
Ejecución: imprimir en pantalla 4 opciones diferentes. Solicitar que se elija una opción y la guarde en una variable.
Valor de retorno: opción elegida
'''

def menu():
    option = int(input(f"¡Bienvenido! Por favor, elija una de las opciones siguientes. \n1. Mensaje\n2. Cálculo de porcentaje\n3. Cerrar programa\n SELECCIÓN: "))
    return option

eleccion = menu()


def encabezado(msg):
     print("1. ID: 000570378\n2. Semestre actual: 2do\n3. Carrera que curso: Ingeniería Aeronáutica") 
     print(msg)

def porcentaje(a, b):
     op = a*(b/100)
     return op

def close():
     print("Cerrando programa")

match eleccion:
        case 1:
            mensaje = str(input("Ingrese un mensaje: "))
            encabezado(mensaje)
        case 2:
            pass
            a = int(input("Ingrese un número: "))
            pct = int(input("¿Qué porcentaje desea aplicarle al número? "))
            op = porcentaje(a, pct)
            print(f"El {pct}% de {a} es {op}")
        case 3:
            close()

'''
# Esta es una función que creé por práctica, no es un ejercicio propuesto en clase
def menuT():
    option = int(input(f"¡Bienvenido! Por favor, elija una de las opciones siguientes. \n1. Boletos aéreos\n2. Toures\n3. Alojamiento\n4. Salir\n SELECCIÓN: "))
    return option

def travelassist():
            print("Usted ha seleccionado la opción 1. TIQUETES AEREOS.")
            print("A continuación, ingrese los siguientes datos.")
            opr = str(input(f"AEROLINEA: "))
            des = str(input(f"DESTINO: "))
            print(f"Usted ha introducido los siguientes datos de viaje:\n Aerolínea: {opr}\n Destino: {des}")
            print("A continuación, ingrese los siguientes datos.")
            traveltype = int(input("Especifique el tipo de boleto:\n1. Ida y regreso\n2. Solo ida\n SELECCIÓN: "))
            if traveltype == 1:
                 depart = str(input("FECHA DE SALIDA: "))
                 arrive = str(input("FECHA DE REGRESO: "))
                 print(f"Usted ha introducido los siguientes datos de viaje:\n Fecha de salida: {depart}\n Destino: {arrive}")
            elif traveltype == 2:
                 depart = str(input("FECHA DE SALIDA: "))
                 print(f"Usted ha introducido los siguientes datos de viaje:\n Fecha de salida: {depart}")
            else:
                 print("La opción ingresada no es válida.")
                 print()
'''
