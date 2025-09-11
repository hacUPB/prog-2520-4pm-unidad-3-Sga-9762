### [```Para visualizar el código de cada ejercicio, click aquí```](RetoUnidad3.py)

# **Ejercicio 1: Simulador de Ascenso y Control de Presurización**

**Contexto Aeronáutico:**
A medida que un avión gana altitud, la presión del aire exterior disminuye drásticamente. Para que los pasajeros y la tripulación puedan respirar con normalidad, la cabina del avión se mantiene presurizada artificialmente. Esto crea una "altitud de cabina" que es mucho menor que la altitud real del avión (generalmente, se mantiene por debajo de los 8,000 pies). Un fallo en este sistema durante el ascenso es una emergencia grave.

**Descripción del Problema:**
Tu objetivo es desarrollar un programa que simule el ascenso de un avión desde el nivel del mar hasta su altitud de crucero. Durante la simulación, el programa debe monitorear el sistema de presurización para asegurar que la "altitud de cabina" se mantenga dentro de los límites de seguridad.

**Requisitos de la Simulación:**

1.  **Estado Inicial:**
    *   El avión comienza en tierra (altitud = **0 pies**).
    *   La altitud de crucero objetivo es de **20,000 pies**.
    *   El límite máximo de seguridad para la altitud de cabina es de **8,000 pies**.
    *   La simulación ocurrirá en "pasos" de ascenso de **1,000 pies** cada uno.

2.  **Proceso de Ascenso (Bucle):**
    *   El programa debe usar un **bucle** para simular el ascenso. En cada iteración del bucle, la altitud del avión aumentará en 1,000 pies.
    *   En cada paso, el programa debe mostrar la **altitud actual del avión** y la **altitud actual de la cabina**.

3.  **Sistema de Presurización (Función y Condicionales):**
    *   Por cada 1,000 pies que sube el avión, la "altitud de cabina" solo debe aumentar en **250 pies**, simulando un ascenso gradual y cómodo.
    *   Dentro del bucle, debes usar un **condicional** para comprobar si la altitud de la cabina ha superado el límite de seguridad de 8,000 pies. Si esto ocurre, el sistema ha "fallado".

4.  **Fin de la Simulación:**
    *   Si la altitud de la cabina supera el límite de seguridad, el bucle debe detenerse inmediatamente y el programa debe mostrar un mensaje de **"¡ALERTA! Fallo de presurización. Iniciando descenso de emergencia."**
    *   Si el avión alcanza los 20,000 pies sin que la cabina supere el límite, el programa debe mostrar un mensaje de **"Ascenso completado. El avión ha alcanzado la altitud de crucero de forma segura."**

---


# Tabla de Datos para la Simulación de Ascenso

| Parámetro | Nombre de Variable | Tipo de Variable | Tipo de Dato | Valor(es) Iniciales / Reglas |
| :--- | :--- | :--- | :--- | :--- |
| **Altitud de Crucero** | `altitud_crucero` | De Entrada / Constante | Entero (`int`) | `20000` |
| **Altitud del Avión** | `altitud_avion` | De Control / Proceso | Entero (`int`) | Inicia en `0`. Se incrementa en cada ciclo. |
| **Paso de Ascenso** | `paso_ascenso` | De Entrada / Constante | Entero (`int`) | `1000` |
| **Altitud de la Cabina** | `altitud_cabina` | De Control / Proceso | Entero (`int`) | Inicia en `0`. Se recalcula en cada ciclo. |
| **Límite de Seguridad** | `limite_seguridad_cabina` | De Entrada / Constante | Entero (`int`) | `8000` |
| **Tasa de Aumento (Cabina)** | `tasa_aumento_cabina` | De Entrada / Constante | Entero (`int`) | `250` |
| **Condición de Éxito** | (No es una variable, es una expresión) | De Control | Booleano (`bool`) | Se evalúa como `altitud_avion >= altitud_crucero`. |
| **Condición de Fallo** | (No es una variable, es una expresión) | De Control | Booleano (`bool`) | Se evalúa como `altitud_cabina >

---





# **Ejercicio 2: Simulador de Gestión del Centro de Gravedad (CG)**

**Contexto Aeronáutico:**
El Centro de Gravedad (CG) es el punto de equilibrio de un avión y es crítico para su estabilidad. Durante un vuelo, el CG se desplaza a medida que se consume el combustible de los diferentes tanques. Si el CG se mueve fuera de los límites permitidos (demasiado adelante o demasiado atrás), el avión puede volverse inestable y peligroso de volar.

**Descripción del Problema:**
Tu tarea es crear un programa que simule un vuelo de 5 horas. Durante la simulación, el usuario (actuando como piloto) deberá tomar decisiones sobre de qué tanques de combustible consumir para mantener el Centro de Gravedad (CG) dentro de un rango seguro.

**Requisitos de la Simulación:**

1.  **Estado Inicial:**
    *   La simulación representa un vuelo de **5 horas**.
    *   El CG inicial del avión es de **22.5%**.
    *   Los límites de seguridad para el CG son: **20.0%** y **25.0%**.

2.  **Proceso Interactivo (Bucle):**
    *   El programa debe avanzar en un **bucle** que simule el paso del tiempo, ejecutándose una vez por cada hora de vuelo.
    *   En cada hora, el programa debe mostrar al usuario la **hora de vuelo actual** y la **posición actual del CG**.

3.  **Toma de Decisiones (Condicionales e Interacción):**
    *   Cada hora, el programa debe preguntar al usuario de qué grupo de tanques desea consumir combustible:
        *   **Opción 1: Tanques de las alas.** Consumir de aquí mueve el CG hacia atrás en `0.3%`.
        *   **Opción 2: Tanque central.** Consumir de aquí mueve el CG hacia adelante en `0.5%`.
    *   El programa debe verificar si el CG está fuera de los límites de seguridad. Si lo está, debe mostrar una **alerta de "ESTABILIDAD CRÍTICA"** antes de pedirle al usuario que tome la siguiente decisión.

4.  **Uso de Funciones:**
    *   Debes crear y utilizar al menos una **función propia**. Por ejemplo, una función llamada `recalcular_cg` que reciba el CG actual y la opción del usuario, y devuelva la nueva posición del CG.

5.  **Fin de la Simulación:**
    *   Al terminar las 5 horas de vuelo, el programa debe mostrar un mensaje final indicando si el aterrizaje fue seguro (CG dentro de los límites) o peligroso (CG fuera de los límites), mostrando la posición final del CG.

| TABLA DE VARIABLES (PROBLEMA 2) |

Variables de entrada:

- Fuel_Wings = variable booleana que indica si se consumirá combustible de los tanques de las alas; ```type(bool)```
- Fuel_Fuselage = variable booleana que indica si se consumirá combustible de los tanques de las alas ```type(bool)```
- CurrentCG = posición del CG actual del avión ```type(float)```

Variables de salida:
- CG = posición del centro de gravedad (nuevo) del avión ```type(float)```
- NewCHAR_safe = variable booleana que determina si las nuevas características de vuelo (a partir de los datos ingresados y cálculos hechos) son seguras o no. ```type(bool)```


Variables intermedias:
- CG_calc = cálculo del centro de gravedad (nuevo) del avión respecto a los tanques de los que se consumirá combustible (CG-(CG*pctg)) ```type(float)```
- MAC = porcentaje en el cual debe ubicarse el CG respecto a la cuerda del ala (utilizado para verificación de seguridad) (Wing_Chord*0.3) ```type(float)```


Constantes:
- Wing_Chord = cuerda del ala de la aeronave ```type(float)```
- pctg = representa la reducción porcentual del CG de acuerdo al tanque de combustible escogido (0.03 para las alas, 0.05 para el fuselaje) ```type(float)```

# **Ejercicio 3: Sistema de Alerta de Velocidad**

**- Objetivo:** en una aeronave Airbus A320, se instala un código para monitorear la velocidad de la aeronave. El programa monitoreará la velocidad de la aeronave desde su ascenso inicial hasta su aterrizaje, realizando 'i' iteraciones correspondientes a un segundo de vuelo, con base en el tiempo de vuelo (en minutos) introducido por el piloto. En caso de detectarse un exceso de velocidad, se envía una alerta al piloto y esta se registra en el sistema. Al final del vuelo, se muestran todas las alertas detectadas, junto con una puntuación de seguridad de vuelo, respecto a las alertas generadas. Dado que la velocidad del sonido decrece a medida que aumenta la altitud, el sistema monitorea la temperatura en cada iteración, y, con base a esta, determina la velocidad máxima de la aeronave. Así mismo, si se tienen dispositivos hipersustentadores o trenes de aterrizaje desplegados, también determina la velocidad máxima a partir de estos.

## TABLA DE VARIABLES

Variables de entrada: 
- IAS = velocidad indicada de la aeronave ```type(float)```
- t_vuelo = tiempo total del vuelo (desde el ascenso hasta el aterrizaje) (en minutos) ```type(int)```
- OAT = temperatura atmosférica ```type(float)```
- FLAPS = variable booleana que determina el estado de los flaps (true = desplegados / false = retraidos) ```type(bool)```
- LDG_GEAR = variable booleana que determina el estado del tren de aterrizaje (true = desplegado / false = retraido) ```type(bool)```

Variables intermedias:
- MACH = velocidad del sonido (en base a la altitud) = EC_MACH```type(float)```
- FLAP_CFG = 1/2/3/4 - configuración de los flaps (si FLAPS = true), a partir de esta se define la velocidad máxima ```type(int)```
- MAX_IAS = velocidad máxima de la aeronave ```type(float)```
- FLG_TIME = tiempo total de vuelo (en segundos) = t_vuelo*60 ```type(int)```



Variables de salida:
- SPD_ALERT = variable que almacena las alertas generadas por exceso de velocidad. ```type(int)```
- t_vuelo


Variables de control:
- i = iteraciones por segundo de vuelo ```type(int)```

Constantes:
- MACH_0DG = 331m/s o 643,4kts - velocidad del sonido a 0°C ```type(float)```
- SPD_SD_decrease = 0.6m/s por °C - constante que determina la velocidad del sonido respecto a la temperatura ```type(float)```
- EC_MACH = MACH_0DG + (SPD_SD_decrease*OAT) ```type(float)```
- ms_to_kt = 1.94384 -> equivalencia de 1m/s en kts. ```type(float)```

## Pseudocódigo:
```
inicio
MACH_0DG = 331m/s
SPD_SD_decrease = 0.6m/s
SPD_ALERT = 0
FLAP_CFG = 0
MAX_IAS = 0
i = 0
ms_to_kt = 1.94384
Leer t_vuelo #minutos
FLG_TIME = t_vuelo*60
mientras i <= FLG_TIME y FLG > 0
    Leer IAS, Leer OAT, Leer FLAPS, LEER LDG_GEAR
    EC_MACH = MACH_0DG + (SPD_SD_decrease*OAT)
    MAX_IAS = EC_MACH*1.94384
    Si FLAPS == true
        Si FLP_CFG = 1
            MAX_IAS == 238
        Si FLP_CFG == 2
            MAX_IAS = 215
        Si FLP_CFG == 3
            MAX_IAS = 195
        Si FLP_CFG == 4
            MAX_IAS = 186
    Fin Si
    Si LDG_GEAR == true
        MAX_IAS = 250
    Fin Si
    Si IAS >= MAX_IAS
        SPD_ALERT += 1
        Mostrar "¡ALERTA: se ha superado la velocidad MÁXIMA de operación! ¡Reduzca la velocidad inmediatamente! Velocidad registrada: {IAS}kts"
    Fin Si
    i += 1
Mostrar "El vuelo ha finalizado. Se generaron {SPD_ALERT} alertas durante un tiempo de vuelo de {t_vuelo} minutos, en el cual se realizaron {i} iteraciones de control."
fin
```
