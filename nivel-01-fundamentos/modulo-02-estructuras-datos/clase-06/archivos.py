# 1. Creá un archivo "mi_primer_archivo.txt" en modo "w" y escribí 3 líneas:
#    "Hola, soy Belén"
#    "Estoy aprendiendo Python"
#    "Hoy es clase de archivos"
#    (recordá los \n al final de cada línea)
# 2. Verificá: andá a la carpeta en el explorador de Windows y abrí el archivo.

"""with open("mi_primer_archivo.txt", "w", encoding="utf-8") as f:
    f.write("Hola, soy Belen\n")
    f.write("Estoy aprendiendo python\n")
    f.write("Hoy es clase de archivos\n")"""

# A) Leé el archivo entero con .read() e imprimilo.
# B) Leé el archivo línea por línea con for e imprimí cada una (con strip()).
# C) Contá cuántas líneas tiene.

"""with open("mi_primer_archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)

with open("mi_primer_archivo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())    

with open("mi_primer_archivo.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
print(len(lineas))"""


# REPORTE DE CAMPAÑAS - Genero un archivo llamado reporte_de_camanas.txt

campanas = [
    {"cliente": "Coolsmart",  "plataforma": "Facebook",  "gastado": 32000, "conversiones": 45},
    {"cliente": "Q-Electric", "plataforma": "Instagram", "gastado": 28500, "conversiones": 38},
    {"cliente": "Danieluk",   "plataforma": "Facebook",  "gastado": 65000, "conversiones": 92},
    {"cliente": "NuevoA",     "plataforma": "Facebook",  "gastado":  9500, "conversiones": 11}
]

total_gastado = sum([c["gastado"] for c in campanas])
total_conv = sum([c["conversiones"] for c in campanas])

from datetime import datetime
fecha_hoy = datetime.now().strftime("%d/%m/%Y")


with open("reporte_de_campanas.txt", "w", encoding="utf-8") as f:
    
    f.write("=" * 35 + "\n")
    f.write("REPORTE SEMANAL DE CAMPAÑAS\n")
    f.write(f"Fecha: {fecha_hoy}\n")
    f.write("=" * 35 + "\n\n")

    
    for c in campanas:
        costo_conv = round(c["gastado"] / c["conversiones"], 2)
        f.write(f"{c['cliente']} ({c['plataforma']})\n")
        f.write(f"  Gastado: ${c['gastado']:,}\n")
        f.write(f"  Conversiones: {c['conversiones']}\n")
        f.write(f"  Costo/conv: ${costo_conv}\n\n")
    
    
    f.write("=" * 35 + "\n")
    f.write(f"TOTAL GASTADO: ${total_gastado:,}\n")
    f.write(f"TOTAL CONVERSIONES: {total_conv}\n")
    f.write("=" * 35 + "\n")


print("\n--- REPORTE GENERADO ---\n")
with open("reporte_de_campanas.txt", "r", encoding="utf-8") as f:
    print(f.read())