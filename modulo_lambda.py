# modulo_lambda.py
from gestion_inventario import inventario

# --- FILTRADO ---
# Queremos solo los sensores ubicados en "Planta_Norte"
# filter() devuelve un objeto, así que lo convertimos en lista
sensores_criticos = list(filter(
    lambda comp: comp["tipo"] == "Sensor" and comp["ubicacion"] == "Planta_Norte",
    inventario
))

# --- MAPEO ---
# Extraemos solo los IDs de esos sensores críticos
ids_sensores = list(map(lambda comp: comp["id"], sensores_criticos))

# --- RESULTADOS ---
print("Sensores críticos encontrados:")
for s in sensores_criticos:
    print(s)

print("\nIDs de sensores críticos:")
print(ids_sensores)
