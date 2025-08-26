#print(10 > 5)
#print("Hola" != "Mundo")
#print(3.14 <= 4.5)
#nombre = "Juan"
#print(nombre == "Juan")
#print(7 > 9)
#print("Hola" == "Adios")

#edad = int(input("Por favor, ingresa tu edad: "))

# Ejercicio 1

#if edad >= 0:
    #if edad <= 5:
     #   etapa = "Primera Infancia"
    #elif edad <= 11:
     #   etapa = "Infancia"
    #elif edad <= 26:
     #   if edad <= 18:
      #      etapa = "Adolescencia y Juventud"
       # elif edad > 18:
        #    etapa = "Juventud"
    #elif edad <= 59:
     #   etapa = "Adultez"
    #else:
     #   etapa = "Persona Mayor (Envejecimiento y Vejez)"
    
    #print(f"Tu etapa del ciclo de vida es: {etapa}")
#else:
 #   print("La edad ingresada no es válida.")

# Ejercicio 2 
print("¡Bienvenido al servicio de envíos de paquetería internacional!")
zona = int(input("1. Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\n  **Seleccione la zona a la que enviará el paquete:** "))

if zona > 0 and zona <= 5:
    peso = float(input("Ingrese el peso del paquete (gramos): "))
    if peso <= 5000 and peso > 0:
            if zona == 1:
                PR = 11 * peso
            elif zona == 2:
                PR = 10 * peso
            elif zona == 3:
                PR = 12 * peso
            elif zona == 4:
                PR = 24 * peso
            elif zona == 5:
                PR = 27*peso
            print(f"El costo total de su envío es ${PR}. **¡Gracias por utilizar nuestros servicios!**")
    else:
        print("No se da el servicio a paquetes con un peso superior a 5000 gramos")
else:
    print("La zona ingresada no existe")
        

