# Datos Del Inventario

inventario = [
    {"id": 1, "nombre": "Sensor de temperatura", "tipo": "sensor"},
    {"id": 2, "nombre": "Motor hidráulico", "tipo": "motor"},
    {"id": 3, "nombre": "Válvula de presión", "tipo": "valvula"},
    {"id": 4, "nombre": "Sensor de humedad", "tipo": "sensor"},
    {"id": 5, "nombre": "Motor eléctrico", "tipo": "motor"}
]

# Listas vacías de clasificar

sensores = []
motores = []
valvulas = []

# Clasificación de componentes(for- if- elif- else)

for componente in inventario:
    tipo = componente["tipo"]
    
    if tipo == "sensor":
        sensores.append(componente["id"])
    elif tipo == "motor":
        motores.append(componente["id"])
    else:
        valvulas.append(componente["id"])

# Resultados en consola

print(" Sensores:", sensores)
print(" Motores:", motores)
print(" Válvulas:", valvulas)


# Simulador de Llenado de Tanque

volumen_actual = 0 # inicio del volumen
tasa_flujo = 50.5  # litros por minuto
capacidad_tanque = 1000 # maximo volumen del tanque

while volumen_actual < capacidad_tanque:
    volumen_actual += tasa_flujo
    print(f"Volumen actual: {volumen_actual:.2f} litros")
    
    if volumen_actual > 950:
        print(" ALERTA: Tanque casi lleno.")
        break  # Detener el bucle antes de desbordar

print(" Simulación de llenado detenida.")
