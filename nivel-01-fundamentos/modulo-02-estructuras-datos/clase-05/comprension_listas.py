# Base de datos (copiá esto arriba del archivo)
clientes = [
    {"nombre": "Coolsmart", "servicio": "LinkedIn",   "facturacion": 180000, "activo": True},
    {"nombre": "Q-Electric","servicio": "LinkedIn",   "facturacion":  95000, "activo": True},
    {"nombre": "Danieluk",  "servicio": "Meta Ads",   "facturacion": 220000, "activo": False},
    {"nombre": "NuevoA",    "servicio": "LinkedIn",   "facturacion":  60000, "activo": True},
    {"nombre": "NuevoB",    "servicio": "Consultoría","facturacion": 150000, "activo": True}
]

# A) Lista de todos los nombres
# B) Lista de nombres de clientes activos
# C) Lista de nombres de clientes que facturan más de 100000

nombres = [c["nombre"] for c in clientes]
print(nombres)
nombres_activos = [c["nombre"] for c in clientes if c["activo"]]
print(nombres_activos)
grandes = [c["nombre"] for c in clientes if c["facturacion"]> 100000]
print(grandes)

# ------------------------------------------
precios = [150, 300, 89, 1200, 450, 780]

# A) Lista de precios en dólares (dividí cada uno por 1000)
# B) Lista de precios con IVA incluido (× 1.21)
# C) Lista de precios formateados como strings: ["$150", "$300", ...]

precio_dolares = [n / 1000 for n in precios]
print(precio_dolares)
iva_incluido = [n * 1.21 for n in precios]
print(iva_incluido)
precios_str = [f"${p}" for p in precios]
print(precios_str)

# -------------------------------------
# A) Dict {nombre: servicio} para todos
# B) Dict {nombre: facturacion} solo de los activos
# C) Dict {nombre: facturacion*1.15} (proyección con 15% de aumento)

servicio = {c["nombre"]: c["servicio"] for c in clientes}
print(servicio)
facturacion = {c["nombre"]: c["facturacion"] for c in clientes if c["activo"]}
print(facturacion)
proyeccion = {c["nombre"]: round(c["facturacion"] * 1.15) for c in clientes if c["activo"]}
print(proyeccion)
