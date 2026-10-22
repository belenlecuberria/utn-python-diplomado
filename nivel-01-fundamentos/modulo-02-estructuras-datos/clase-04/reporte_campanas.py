
# Base de campañas Meta Ads — semana del 1 al 7 de octubre
campanas = [
    {
        "cliente": "Coolsmart",
        "plataforma": "Facebook",
        "activa": True ,
        "presupuesto": 50000,
        "gastado": 32000,
        "impresiones": 180000,
        "clicks": 2700,
        "conversiones": 45
    },
    {
        "cliente": "Q-Electric",
        "plataforma": "Instagram",
        "activa": True ,
        "presupuesto": 30000,
        "gastado": 28500,
        "impresiones": 95000,
        "clicks": 1900,
        "conversiones": 38
    },
    {
        "cliente": "Danieluk",
        "plataforma": "Facebook",
        "activa": False ,
        "presupuesto": 80000,
        "gastado": 65000,
        "impresiones": 220000,
        "clicks": 3800,
        "conversiones": 92
    },
    {
        "cliente": "Coolsmart",
        "plataforma": "Instagram",
        "activa": True ,
        "presupuesto": 25000,
        "gastado": 18000,
        "impresiones": 72000,
        "clicks": 1440,
        "conversiones": 24
    },
    {
        "cliente": "NuevoA",
        "plataforma": "Facebook",
        "activa": True ,
        "presupuesto": 15000,
        "gastado": 9500,
        "impresiones": 48000,
        "clicks": 820,
        "conversiones": 11
    }
]

#Ejercicio 1 — listas + dicts + filter+aggregate
#Calculá e imprimí:

#Cantidad total de campañas.
#Cantidad de campañas activas.
#Presupuesto total asignado.
#Gasto total.
#% de ejecución del presupuesto, redondeado a 1 decimal.
#Nombre del cliente de la campaña con MÁS conversiones.

print(len(campanas))
activos = 0
for c in campanas:
    if c["activa"]:
        activos += 1
print(activos)
presupuesto_total = 0
for c in campanas:
    if c["activa"]:
        presupuesto_total += c["presupuesto"]
print(presupuesto_total)
gasto_total = 0
for c in campanas:
    if c["activa"]:
        gasto_total += c["gastado"]
print(gasto_total)
porcentaje = round((gasto_total/presupuesto_total)* 100, 1)
print(f"el porcentaje de ejecución del presupuesto es: {(porcentaje)} %")

top = max(campanas, key=lambda c: c["conversiones"])
print(f"cliente top {top["cliente"]} con {top["conversiones"]} conversiones")

# Ejercicio 2 - Escribir una función calcular_metricas(camp) que reciba un diccionario de campaña y devuelva una tupla 
# con 3 métricas calculadas: CTR, CPC, CRV

def calcular_metricas(c):
    ctr = round(c["clicks"] / c["impresiones"] * 100, 2)
    cpc = round(c["gastado"] / c["clicks"], 2)
    cvr = round(c["conversiones"] / c["clicks"] * 100, 2)
    return ctr, cpc, cvr 
for c in campanas:
    ctr, cpc, cvr = calcular_metricas(c)
    print(f"{c['cliente']} ({c['plataforma']}): CTR {ctr}% | CPC ${cpc} | CVR {cvr}%")

# Ejercicio 3 — Sets aplicados al negocio (sets + operaciones de conjunto)

#Plataformas únicas en las que hay campañas (Facebook, Instagram).
plataformas = set()
for c in campanas:
    plataformas.add(c["plataforma"])
print(f"existen campañas en {(plataformas)}")

#Clientes con al menos una campaña activa
cli_activos = set()
for c in campanas:
    if c["activa"]:                   
        cli_activos.add(c["cliente"]) 
print(f"Clientes con campañas activas: {cli_activos}")

#Clientes con al menos una campaña pausada 
cli_pausados = set()
for c in campanas:
    if not c["activa"]:               
        cli_pausados.add(c["cliente"])
print(f"Clientes con campañas pausadas: {cli_pausados}")

#Clientes que tienen de las dos (intersección) 
#Clientes que SOLO tienen activas (los activos menos los pausados) 
tienen_ambos = cli_activos & cli_pausados       
solo_activos = cli_activos - cli_pausados       

print(f"Clientes con ambos tipos: {tienen_ambos}")
print(f"Clientes 100% activos: {solo_activos}")

# Ejercicio 4 - Reporte final integrador
# Un dict donde la clave es el nombre del cliente, el valor es otro dict con sus totales
resumen_por_cliente = {}

for c in campanas:
    cli = c["cliente"]
    if cli not in resumen_por_cliente:
        
        resumen_por_cliente[cli] = {
            "campanas": 0,
            "gastado": 0,
            "conversiones": 0
        }
    
    resumen_por_cliente[cli]["campanas"] += 1
    resumen_por_cliente[cli]["gastado"] += c["gastado"]
    resumen_por_cliente[cli]["conversiones"] += c["conversiones"]

# Reporte 
print("\n" + "="*50)
print("📊 REPORTE SEMANAL POR CLIENTE")
print("="*50)
for cliente, datos in resumen_por_cliente.items():
    costo_por_conv = round(datos["gastado"] / datos["conversiones"], 2) if datos["conversiones"] > 0 else 0
    print(f"\n👤 {cliente}")
    print(f"   Campañas: {datos['campanas']}")
    print(f"   Gastado:  ${datos['gastado']:,}")
    print(f"   Conv.:    {datos['conversiones']}")
    print(f"   Costo/conv: ${costo_por_conv}")