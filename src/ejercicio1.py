nombre = input("Por favor, ingrese su nombre: ")
print("Bienvenido ", nombre)

# Calcular el IMC (Índice de Masa Corporal): peso / estatura^2
print("CALCULADORA DE INDICE DE MASA CORPORAL")

estatura = float(input("Ingrese su estatura (metros): "))
peso = float(input("Ingrese su peso (kg): "))

IMC = peso / estatura ** 2
print("Su IMC es: ", IMC)

if IMC < 18.49:
    msg = "bajo peso corporal"
elif IMC < 25:
    msg = "normal"
elif IMC < 30:
    msg = "sobrepeso"
elif IMC < 40:
    msg = "obesidad"
else:
    msg = "obesidad EXTREMA"

print(f"{nombre}, su IMC es {IMC:0.2f} y su condición corporal es {msg}.")


