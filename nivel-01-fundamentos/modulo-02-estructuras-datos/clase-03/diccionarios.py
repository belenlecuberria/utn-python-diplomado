# 1. Creá un dict "cliente" con estas claves:
#    nombre, email, servicio_contratado, mes_inicio, facturacion_mensual
#    Usá datos realistas de un cliente ficticio de Trafficker Digital.
# 2. Imprimí cada valor por separado accediendo por clave.
# 3. Agregá una nueva clave "telefono" con un valor.
# 4. Modificá facturacion_mensual (aumentala un 15%).
# 5. Imprimí el dict completo al final.

"""cliente = {"nombre":"DanielukDigital", "email":"servicios@danielukdigital.com", "servicio_contratado":"mediabuyer", "mes_inicio":"febrero", "facturacion_mensual":300000}
print(cliente["nombre"])
print(cliente["email"])
print(cliente["servicio_contratado"])
print(cliente["mes_inicio"])
print(cliente["facturacion_mensual"])
cliente["telefono"]="0112345678"
cliente["facturacion_mensual"]=cliente["facturacion_mensual"] * 1.15
print(cliente)"""
# ============================================
# Ejercicio 2 — Recorrer un diccionario
# ============================================
# 1. Recorrer con .items() e imprimir "{mes}: ${monto}" para cada uno.
# 2. Calcular y mostrar:
#    - Total facturado en el año
#    - Promedio mensual (redondeado a 2 decimales)
#    - Mes con mayor facturación
#    - Mes con menor facturación
# 3. BONUS: cuántos meses superaron el promedio

"""facturacion = {"enero": 15000, "febrero": 18000, "marzo": 22000, "abril": 20000,
    "mayo": 25000,  "junio": 28000,  "julio": 24000, "agosto": 26000, "septiembre": 30000, 
    "octubre": 32000, "noviembre": 29000, "diciembre": 35000}

for mes, monto in facturacion.items():
    print(f"{mes}:{monto}")

total_facturado = sum(facturacion.values())
print(total_facturado)

promedio = round(total_facturado / len(facturacion), 2)
print(promedio)

mes_top = max(facturacion , key=facturacion.get)
mes_low = min(facturacion , key=facturacion.get)
print(mes_top)
print(mes_low)

# meses que superaron el promedio
superiores = 0
for monto in facturacion.values():
    if monto > promedio:
        superiores += 1
print(superiores)"""
# ============================================
# Ejercicio 3 — Base de clientes de Trafficker Digital
# ============================================
# Calculá e imprimí:
# 1. Cantidad total de clientes.
# 2. Cantidad de clientes activos.
# 3. Facturación total de clientes activos.
# 4. Lista de nombres de todos los clientes.
# 5. Lista de nombres de clientes que facturaron más de $100.000.
# 6. El cliente con mayor facturación (nombre + monto).
# 7. BONUS: agregá un nuevo cliente con .append y recorré todo de nuevo.

clientes = [
    {"nombre": "Coolsmart",  "servicio": "LinkedIn",     "facturacion": 180000, "activo": True},
    {"nombre": "Q-Electric", "servicio": "LinkedIn",     "facturacion":  95000, "activo": True},
    {"nombre": "Danieluk",   "servicio": "Meta Ads",     "facturacion": 220000, "activo": False},
    {"nombre": "NuevoA",     "servicio": "LinkedIn",     "facturacion":  60000, "activo": True},
    {"nombre": "NuevoB",     "servicio": "Consultoría",  "facturacion": 150000, "activo": True}
]

print("cantidad de clientes")
print(len(clientes))
print("clientes activos")
cli_activo = 0
for c in clientes:
    if c["activo"]:
        cli_activo += 1
print(cli_activo)
print("facturacion total")
ingreso = 0
for c in clientes:
    if c["activo"]:
        ingreso += c["facturacion"]
print(ingreso)
print("nombres de clientes")
nombres = []
for c in clientes:
    nombres.append(c["nombre"])
print(nombres)
print("quienes facturaron mas de 100k")
nombres1 = []
for c in clientes:
    if c["facturacion"] > 100000:
        nombres1.append(c["nombre"])
print(nombres1)
print("cliente top")
top = max(clientes, key=lambda c : c["facturacion"])
print(f"top {top["nombre"]} con $ {top["facturacion"]}")
# nuevo cliente
clientes.append({"nombre":"nuevoC", "servicio":"mediabuyer", "facturacion":150000, "activo":True})
print("lista modificada")
print(clientes)