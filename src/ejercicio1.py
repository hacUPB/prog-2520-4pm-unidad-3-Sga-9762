#nombre = input("Por favor, ingrese su nombre: ")
#print("Bienvenido ", nombre)

# Calcular el IMC (Índice de Masa Corporal): peso / estatura^2
print("CALCULADORA DE INDICE DE MASA CORPORAL")

estatura = float(input("Ingrese su estatura (metros): "))
peso = float(input("Ingrese su peso (kg): "))

IMC = peso / estatura ** 2
print("Su IMC es: ", IMC)
if IMC < 18.49:
    print("Alerta: USTED tiene un bajo peso corporal")
elif 18.5 < IMC < 24.99:
    print("Su peso corporal es normal")
elif 25 < IMC < 29.9:
    print("Alerta: USTED tiene sobrepeso")
elif 30 < IMC < 39.99:
    print("Alerta: USTED tiene obesidad")
else:
    print("Alerta: USTED tiene obesidad EXTREMA")


