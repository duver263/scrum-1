inventario = [
    {
        "id": "S-101",
        "tipo": "Sensor",
        "ubicacion": "Linea 1",
        "lecturas": [23.5, 24.1, 22.8]
    },
    {
        "id": "M-202",
        "tipo": "Motor",
        "ubicacion": "Linea 2",
        "lecturas": [50.0, 49.5, 50.3]
    },
    {
        "id": "V-303",
        "tipo": "Válvula",
        "ubicacion": "Tanque A",
        "lecturas": [10.2, 9.8, 10.5]
    }
]

# Calcular el promedio de lecturas para un ID específico
id_buscado = "S-101"
promedio = None

for componente in inventario:
    if componente["id"] == id_buscado:
        promedio = sum(componente["lecturas"]) / len(componente["lecturas"])
        break

if promedio is not None:
    print(f"Promedio de lecturas para {id_buscado}: {promedio}")
else:
    print(f"No se encontró el componente con ID: {id_buscado}")
