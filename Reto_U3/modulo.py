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

def Ascenso():
    pass
    

def CG():
    pass

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
            while FLG_TIME > 0 and i <= FLG_TIME:
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
                i += 1
                
            print(f"El vuelo ha finalizado. Se generaron {SPD_ALERT} alertas durante un tiempo de vuelo de {t_vuelo} minutos, en el cual se realizaron {i} iteraciones de control.")
        case 2:
            chc = int(input("¿Iniciar el vuelo?\n 1. SI\n 2. NO\n SU SELECCION: "))
        case _:
              print("El valor ingresado no es válido")
              chc = int(input("¿Iniciar el vuelo?\n 1. SI\n 2. NO\n SU SELECCION: "))
    return SPD_ALERT
