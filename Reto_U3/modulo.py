import random

#OAT = 0
#IAS = 0 
#FLAPS = 0
#LDG_GEAR = 0
#FLAP_CFG = 0

def valuecomputer(OAT, IAS, FLAPS, LDG_GEAR, FLAP_CFG):
            OAT = random.randrange(-56, 40)
            IAS = random.randrange(0, 410)
            FLAPS = random.randrange(0,2)
            LDG_GEAR = random.randrange(0,2)
            FLAP_CFG = random.randrange(0,5)
            return OAT, IAS, FLAPS, LDG_GEAR, FLAP_CFG


def Ascenso(altitud_crucero:int):
    altitud_avion = 0
    altitud_cabina = 0
    paso_ascenso = 1000
    limite_seguridad_cabina = 8000
    tasa_aumento_cabina = 250

    while altitud_avion < altitud_crucero:
        altitud_avion = altitud_avion + paso_ascenso
        altitud_cabina = altitud_cabina + tasa_aumento_cabina
        print(f"La altitud actual del avion es de {altitud_avion} y la altitud de cabina es {altitud_cabina}")
        if altitud_cabina > limite_seguridad_cabina:
            print("¡ALERTA! Fallo de presurizacion.\nIniciando descenso de emergencia")
            break
    
    print("Ascenso completado. El avion ha alcanzado la altitud de crucero de forma segura")


    

def CG(opt, CG):
            if opt == 1:
                        CG = CG - 0.3
            elif opt == 2:
                        CG = CG + 0.5
            return CG

def SpdAlert():
    MACH_0DG = 331
    SPD_SD_decrease = 0.6
    SPD_ALERT = 0
    FLAP_CFG = 0
    MAX_IAS = 0
    i = 0
    ms_to_kt = 1.94384
    OAT = 0
    IAS = 0
    FLAPS = 0 
    LDG_GEAR = 0 
    t_vuelo = int(input("Ingrese el tiempo total de vuelo (en minutos): "))
    FLG_TIME = t_vuelo*60 # tiempo en segundos
    chc = int(input("¿Iniciar el vuelo?\n 1. SI\n 2. NO\n SU SELECCION: "))
    match chc:
        case 1:
            for i in range(0, FLG_TIME + 1):
            # valuecomputer()
                OAT, IAS, FLAPS, LDG_GEAR, FLAP_CFG = valuecomputer(OAT, IAS, FLAPS, LDG_GEAR, FLAP_CFG)
                print(f"**Iteracion: {i}**\n **Temperatura externa: {OAT}°C**\n **Velocidad indicada: {IAS}kts**\n **Estado de flaps: {FLAPS}**\n **Configuracion de flaps: {FLAP_CFG}**\n **Estado del tren de aterrizaje: {LDG_GEAR}**")
                EC_MACH = MACH_0DG + (SPD_SD_decrease*OAT)
                MAX_IAS = EC_MACH*ms_to_kt
                if FLAPS == 1:
                    if FLAP_CFG == 1:
                        #print("FLAPS 1")
                        MAX_IAS = 238
                    elif FLAP_CFG == 2:
                        #print("FLAPS 2")
                        MAX_IAS = 215
                    elif FLAP_CFG == 3:
                        #print("FLAPS 3")
                        MAX_IAS = 195
                    elif FLAP_CFG == 4:
                        #print("FLAPS 4")
                        MAX_IAS = 186

                if LDG_GEAR == 1:
                    MAX_IAS = 250
                if IAS >= MAX_IAS:
                    print(f"¡ALERTA: se ha superado la velocidad MÁXIMA de operación! ¡Reduzca la velocidad inmediatamente!\n Velocidad máxima: {MAX_IAS}kts \n Velocidad registrada: {IAS}kts")
                    SPD_ALERT += 1
                #i += 1
                
            print(f"El vuelo ha finalizado. Se generaron {SPD_ALERT} alertas durante un tiempo de vuelo de {t_vuelo} minutos, en el cual se realizaron {i} iteraciones de control.")
        case 2:
            chc = int(input("¿Iniciar el vuelo?\n 1. SI\n 2. NO\n SU SELECCION: "))
        case _:
              print("El valor ingresado no es válido")
              chc = int(input("¿Iniciar el vuelo?\n 1. SI\n 2. NO\n SU SELECCION: "))
    return SPD_ALERT

def fuelsim():
            #initCG = 22.5
            uprLMT = 25
            lwrLMT = 20
            #chgWING = -0.3
            #chgCTR = 0.5
            flt = int(input("Ingrese la duración del vuelo (horas): "))
            currentCG = 22.5
            i = 0
            while i <= flt and flt < 20 and flt > 0:
                        print(f"Iteración actual: {i}")
                        opcion_tanque = 0
                        opcion_tanque = int(input(f"Seleccione la sección de tanques de combustible a consumir:\n 1. ALAS\n 2. FUSELAJE CENTRAL\n **¡IMPORTANTE! RANGO DE CG SEGURO: entre 20% y 25%\n CG actual: {currentCG}\n SU SELECCION: "))
                        if opcion_tanque == 1:
                                    currentCG = CG(opcion_tanque, currentCG)
                        elif opcion_tanque == 2:
                                    currentCG = CG(opcion_tanque, currentCG)
                        if uprLMT < currentCG :
                                    print("¡ALERTA! ESTABILIDAD CRITICA. MODIFIQUE EL CENTRO DE GRAVEDAD INMEDIATAMENTE")
                        i += 1
            if lwrLMT < currentCG < uprLMT and flt < 20 and flt > 0:
                        print(f"¡Aterrizaje seguro! CG actual: {currentCG}")
            elif currentCG < lwrLMT or currentCG > uprLMT:
                        print(f"¡ATERRIZAJE PELIGROSO! CG actual: {currentCG}")
            if flt > 20 or flt < 0:
                   print("El tiempo de vuelo ingresado no es válido.")
            return currentCG
                                    
                        
