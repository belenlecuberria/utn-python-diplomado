
# 1. Creá una tupla con tus 3 clientes actuales de Trafficker Digital
# 2. Imprimí:
#    - El primer cliente
#    - El último cliente usando índice negativo
#    - La cantidad total
# 3. Intentá cambiar el primer cliente:
#    clientes[0] = "NuevoCliente"
#    ¿Qué error te da? Copiá el mensaje del error como comentario.
# 4. Hacé una tupla "clientes_nueva" que agregue "NuevoCliente" al final.
#    Pista: usá concatenación con el operador +

"""clientes = ("Coolsmart", "Q-Electric", "Danieluk")
print(clientes[0])
print(clientes[-1])
print(len(clientes))

clientes[0] = "Nuevo"  #TypeError: ¨tuple¨ object does not support item assignment

clientes_nueva = clientes.append("NuevoCliente")   #AttributeError: ¨Tuple¨ object has no attribute ´append´
print(clientes_nueva)

clientes_nueva = clientes + ("NuevoCliente", )
print(clientes_nueva)"""

# 1. Creá una función que reciba una lista de likes y devuelva:
#    el máximo, el mínimo y el promedio (como tupla).
# 2. Llamala con esta lista:
# 3. Desempaquetá el resultado en 3 variables:
# 4. Imprimí cada una con un mensaje descriptivo.

"""likes = [45, 128, 87, 23, 210, 62, 91, 34, 78, 156]

def analizar(likes):
    return min(likes), max(likes), sum(likes)/len(likes)

minimo, maximo, promedio = analizar(likes)
print("el minimo de likes es", minimo)
print("el maximo de likes es", maximo)
print("el promedio de likes es", promedio)"""


# conjuntos
# Clientes con los que trabajaste cada año
#clientes_2025 = {"Coolsmart", "Q-Electric", "Danieluk", "ExCliente1", "ExCliente2"}
#clientes_2026 = {"Coolsmart", "Danieluk", "NuevoA", "NuevoB"}

# Calculá e imprimí:
# 1. Total de clientes únicos entre ambos años (unión).
# 2. Clientes que RENOVARON (están en los dos años → intersección).
# 3. Clientes PERDIDOS (estaban en 2025 pero no en 2026 → diferencia).
# 4. Clientes NUEVOS en 2026 (no estaban en 2025 → diferencia inversa).
# 5. Tasa de retención: (renovados / clientes_2025) × 100, redondeada a 1 decimal.

# BONUS: convertí esta lista en un set para quitar duplicados,
# y mostrá cuántos emails únicos hay:
#emails = ["a@a.com", "b@b.com", "a@a.com", "c@c.com", "b@b.com", "d@d.com"]


clientes_2025 = {"Coolsmart", "Q-Electric", "Danieluk", "ExCliente1", "ExCliente2"}
clientes_2026 = {"Coolsmart", "Danieluk", "NuevoA", "NuevoB"}

print("total de clientes únicos")
clientes_unicos = clientes_2025.union(clientes_2026)
print(clientes_unicos)
print("renovaciones")
renov = clientes_2025.intersection(clientes_2026)
print(renov)
print("clientes perdidos")
perdidos = clientes_2025.difference(clientes_2026)
print(perdidos)
print("clientes nuevos")
nuevos = clientes_2026.difference(clientes_2025)
print(nuevos)
print("tasa de retención de clientes")
tasa_retencion = round(len(renov) / len(clientes_2025) * 100, 1)
print(tasa_retencion, "%")

print("_______________")

emails = ["a@a.com", "b@b.com", "a@a.com", "c@c.com", "b@b.com", "d@d.com"]
emails_unicos = set(emails)
print(f"emails unicos: {len(emails_unicos)}")
print(emails_unicos)