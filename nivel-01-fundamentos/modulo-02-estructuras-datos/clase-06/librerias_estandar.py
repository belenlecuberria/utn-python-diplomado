# Un cliente te deja $100.000 para invertir en pauta publicitaria durante 12 meses, 
# con una reinversión mensual del 5% de ganancias. Calculá cuánto termina siendo al final.

# monto_final = capital_inicial * (1 + tasa) ** meses

import math

capital = 100000
tasa = 0.05       
meses = 12

monto_final = capital * math.pow(1 + tasa, meses)

print(f"Capital inicial: ${capital:,}")
print(f"Después de {meses} meses: ${round(monto_final, 2):,}")
print(f"Ganancia total: ${round(monto_final - capital, 2):,}")

tiempo_duplicar = math.log(2) / math.log(1 + tasa)
print(f"Tiempo para duplicar: {round(tiempo_duplicar, 1)} meses")


# 1. Para cada campaña, simulá las conversiones reales
#    con una variación de ±20% usando random.uniform(-0.20, 0.20)
#    y guardalas en el mismo dict con la clave "conversiones_reales"

# 2. Después imprimí:
#    "Coolsmart: esperadas 45 → reales 48 (variación +6.7%)"

# BONUS: elegí al azar 1 campaña ganadora del mes con random.choice()

import random

random.seed(42)   

campanas = [
    {"cliente": "Coolsmart",  "conversiones_esperadas": 45},
    {"cliente": "Q-Electric", "conversiones_esperadas": 38},
    {"cliente": "Danieluk",   "conversiones_esperadas": 92}
]

for c in campanas:
    variacion = random.uniform(-0.20, 0.20)   
    c["conversiones_reales"] = round(c["conversiones_esperadas"] * (1 + variacion))
    c["variacion_%"] = round(variacion * 100, 1)

for c in campanas:
     print(f"{c['cliente']}: esperadas {c['conversiones_esperadas']} - reales {c['conversiones_reales']}, variación {c['variacion_%']}%")
        

ganadora = random.choice(campanas)
print(f"La campaña ganadora es: {ganadora['cliente']}")


#Tenés una campaña que arranca el 24 de noviembre de 2026 a las 00:00 y dura 5 días.
#Calculá e imprimí:

# 1. Definí la fecha/hora de inicio de la campaña

# 2. Calculá la fecha de fin (inicio + 5 días)

# 3. Imprimí:
#    - Inicio formateado como "lunes 24 de November de 2026 a las 00:00"
#    - Fin formateado igual
#    - Cuántos días faltan desde hoy hasta el inicio (podés restar dates)
#    - Si hoy ya pasó el inicio, imprimí "La campaña YA está activa"
#      (usá un if comparando datetime.now() con inicio)

# BONUS: generá una lista con las 5 fechas que durará la campaña
#        (inicio, inicio + 1 día, inicio + 2 días, ..., inicio + 4 días)
#        e imprimilas una por línea.

from datetime import datetime, timedelta

hoy = datetime.today()
inicio = datetime(2026, 11, 24, 0, 0)
fin = inicio + timedelta(days = 5)
print(f"inicio de campaña: {inicio.strftime('%d de %B de %Y')}")
print(f"fin de campaña: {fin.strftime('%d de %B de %Y')} ")

if hoy < inicio:
    print(f"faltan {inicio - hoy} días para el inicio")
else:
    print("La campaña ya ha iniciado")

dias_campana = [inicio + timedelta(days = d) for d in range(5)]
for fecha in dias_campana:
    print(fecha.strftime("%A %d/%m"))
