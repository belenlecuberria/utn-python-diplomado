paises = ["Argentina", "Uruguay", "Chile", "Brasil", "Paraguay", "Bolivia"]
print(len(paises))
print(paises[0])
print(paises[-1])
print(paises[2])
print("########")

print(paises[:3])
print(paises[4:])
print(paises[2:4])
print(paises[::-1])
print("########")

carrito = ["pan","leche"]
carrito.append("huevos")
print(carrito)
carrito.insert(0,"cafe")
print(carrito)
carrito2 = ["azucar","manteca"]
carrito.extend(["azucar","manteca"])
len(carrito)
print(carrito)
print("#########")

precios = [150, 300, 89, 1200, 450, 780]
print(precios)
for p in precios:
      print(f"$ {p}")
print("la suma de todos los precios es")
print(sum(precios))
print("el promedio de todos los precios es")
print(sum(precios)//len(precios))

caros = 0
for p in precios:
        if p > 500:
            caros = caros +1
print ("hay", caros, "productos caros")

print("#######")
notas = [7, 4, 9, 10, 6, 5, 8, 3, 7, 10]
print(notas)
print("la nota maxima es")
print(max(notas))
print("la nota mínima es")
print(min(notas))
print("el 10 aparece", (notas.count(10)), "veces")
print(notas.index(10))
print(4 in notas)
print(sorted(notas, reverse=True))
print(notas)
