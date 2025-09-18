
'''
#while numero >= 20 and numero <= 80:
 #   if numero % 2 == 0:
  #       print(numero)
   #      numero += 1
   # else:
    #     numero += 1
            
#while numero <= 99 and numero >= 61:
 #   if numero % 2 != 0:
  #       print(numero)
   # numero -= 1
'''


'''
n1 = int(input("Ingrese un número:"))
n2 = int(input("Ingrese otro número:"))

if n1 > n2:
    numberup = n1
    numberdw = n2 
else:
    numberup = n2
    numberdw = n1

while numberdw <= numberup:
    if numberdw % 2 != 0:
        print(numberdw) 
    numberdw += 1
'''
'''
numero = 0

while numero >= 0 and numero <= 1000:
    if numero %7 == 0:
        print(numero)
    numero += 1 
'''

'''
numero = int(input("Ingrese un número: "))
i = 0
while i <= 15:
    ct = numero *i
    print(f"{numero} x {i} = {ct}")
    i += 1
'''
'''
# Menú 2

control = True

while control == True:
    print("**¡Bienvenido a nuestro restaurante!**\n1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres"\
      "\n5. Salir")
    opt = int(input("Seleccione una de las anteriores opciones: "))
    match opt:
        case 1:
            print("**MENÚ: ENTRADAS**\n1. Patacón\n2. Yuca\n3. Arepa\n4. Papas a la francesa")
            print()
        case 2:
            print("**MENÚ: PLATOS FUERTES**\n1. Solomito\n2. Pollo a la plancha\n3. Cerdo a la plancha\n4. Ajiaco")
            print()
        case 3:
            print("**MENÚ: BEBIDAS**\n1. Limonadas\n2. Jugos naturales\n3. Té\n4. Cervezas")
            print()
        case 4:
            print("**MENÚ: POSTRES**\n1. Cheesecake\n2. Tiramisú\n3. Tortas\n4. Creme Bruleé")
            print()
        case 5:
            control = False
        case _:
            print("**Opción Inválida**")
            print()
'''

'''
numero = int(input("Ingrese un número para la sucesión: "))


if numero == 1:
    print(0)
elif numero >= 1:
    a = 0
    b = 1
    m = 1
    print("**Inicializando**")
    print(a,b)

    while m <= (numero - 2):
        c = a +b
        print(c)
        a = b
        b = c
        m = m + 1
    print("**Sucesión terminada. No se imprimen más términos**")
elif numero <= 0:
    print("No se imprimen terminos")
'''

'''
numero = int(input("Ingrese un número: "))
i = 0
while i <= 10:
    pr = numero*i
    print(f"{numero} x {i} = {pr}")
    i = i + 1
'''
# Bucle 'for':
'''
numero = int(input("Ingrese un número positivo: "))
for numero in range(numero+1):
    if numero%2 == 0:
        print(f"**Número par encontrado: {numero}**")
        b = numero 
        c = numero + b 
print(f"La suma de los números pares desde 0 hasta {numero} es {c}")
'''
'''
numero = int(input("Ingrese un número positivo: "))
i = 0 
j = 0
for i in range(1, numero+1):
    for j in range(1, i + 1):
        print(j,end=' ')
    print()
'''
'''
# Adivinar número
#import random
from random import randint
# Si se importa un módulo, y deseo usar funciones de ese módulo, debo llamar primero al módulo seguido de la función (ej: random.funcion)
num_ran = randint(1, 100)
numero = -1
i = 0

while numero != num_ran:
    i = i + 1
    numero = int(input("Adivina el número generado (entre 0 y 100):) -> "))
    if numero > num_ran:
        print("El número generado es menor")
    elif numero < num_ran:
        print("El número generado es mayor")
    else:
        print(f"El número ingresado es **correcto!**. Intentos totales: {i}")
'''

# Verificador de # primo

num = int(input("Ingrese un número entero mayor que 1: "))
divisor = num // 2 
cont = 0
for i in range(2, divisor + 1 ):
    if num % i == 0:
        cont += 1 

if cont == 0:
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")
    for i in range(1, num+1):
        if num % i == 0:
            print(i)


