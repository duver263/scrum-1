# modulo_analisis.py
from gestion_inventario import inventario

def analizar_componente(componente_dict):
    """
    Recibe un diccionario de componente y calcula:
    promedio, máximo y mínimo de sus lecturas.
    Retorna un nuevo diccionario con los resultados.
    """
    lecturas = componente_dict.get("lecturas", [])

    if not lecturas:
        return {"promedio": None, "max": None, "min": None}

    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)

    return {"promedio": promedio, "max": maximo, "min": minimo}


# 🔹 Prueba de la función con un componente del inventario
if __name__ == "__main__":
    componente = inventario[0]  # Primer componente del inventario
    resultado = analizar_componente(componente)
    print(f"Análisis del componente '{componente['id']}':")
    print(resultado)
