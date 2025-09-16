import random

OAT = 0
IAS = 0 
FLAPS = 0
LDG_GEAR = 0

def valuecomputer(OAT, IAS, FLAPS, LDG_GEAR):
            OAT = random.randrange(-56, 40)
            IAS = random.randrange(0, 500)
            FLAPS = random.randrange(0,2)
            LDG_GEAR = random.randrange(0,2)
            FLAP_CFG = random.randrange(0,5)
            return OAT, IAS, FLAPS, LDG_GEAR

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
    while FLG_TIME > 0 and i <= FLG_TIME:
       # valuecomputer()
        OAT, IAS, FLAPS, LDG_GEAR = valuecomputer(OAT, IAS, FLAPS, LDG_GEAR)
        print(f"iteracion: {i}", OAT, IAS, FLAPS, LDG_GEAR)
        EC_MACH = MACH_0DG + (SPD_SD_decrease*OAT)
        MAX_IAS = EC_MACH*ms_to_kt
        if FLAPS == 1:
            if FLAP_CFG == 1:
                MAX_IAS = 238
            elif FLAP_CFG == 2:
                MAX_IAS = 215
            elif FLAP_CFG == 3:
                MAX_IAS = 195
            elif FLAP_CFG == 4:
                MAX_IAS = 186

        if LDG_GEAR == 1:
            MAX_IAS = 250
        if IAS >= MAX_IAS:
            SPD_ALERT =+ 1
            Warning(f"¡ALERTA: se ha superado la velocidad MÁXIMA de operación! ¡Reduzca la velocidad inmediatamente! Velocidad registrada: {IAS}kts")
        i += 1
        
    print(f"El vuelo ha finalizado. Se generaron {SPD_ALERT} alertas durante un tiempo de vuelo de {t_vuelo} minutos, en el cual se realizaron {i} iteraciones de control.")
    return SPD_ALERT