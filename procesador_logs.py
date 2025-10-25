# procesador_logs.py
# Módulo 2 - Ejercicios con Strings

print("="*60)
print("EJERCICIO 1: DECODIFICADOR DE REPORTE")
print("="*60)

# Aquí tenemos el reporte que llega como un solo texto largo
reporte = "ID_SENSOR:T-21,LOC:Planta_Norte,TEMP:45.8,STATUS:OK"

# Primero lo partimos por las comas para separar cada pedazo de información
campos = reporte.split(',')

# Ahora extraemos los valores que nos interesan
# Básicamente dividimos cada campo por los dos puntos y agarramos lo que está después
id_sensor = campos[0].split(':')[1]  # Sacamos el ID del sensor
localizacion = campos[1].split(':')[1]  # Sacamos dónde está ubicado
temperatura_str = campos[2].split(':')[1]  # Sacamos la temperatura (todavía como texto)
status = campos[3].split(':')[1]  # Sacamos el estado

# Como la temperatura nos sirve más como número, la convertimos a float
temperatura = float(temperatura_str)

# Ahora imprimimos todo bonito y ordenado
print("\n*** REPORTE DE SENSOR ***")
print(f"ID: {id_sensor}")
print(f"Ubicación: {localizacion}")
print(f"Temperatura: {temperatura} °C")
print(f"Estado: {status}")

print("\n" + "="*60)
print("EJERCICIO 2: VALIDADOR DE LOTE")
print("="*60)

# Esta función revisa si un código de lote cumple con las reglas
def validar_lote(codigo_lote):
    """
    Revisa que el código de lote cumpla con todo lo que necesitamos:
    - Que tenga exactamente 12 caracteres
    - Que empiece con "LOT-"
    - Que termine con "-24"
    - Que el octavo carácter sea una 'X' o una 'Y'
    """
    print(f"\nValidando código: {codigo_lote}")
    
    # Vamos checando cada regla una por una
    regla1 = len(codigo_lote) == 12
    print(f"  ✓ Longitud 12 caracteres: {regla1} (actual: {len(codigo_lote)})")
    
    regla2 = codigo_lote.startswith("LOT-")
    print(f"  ✓ Empieza con 'LOT-': {regla2}")
    
    regla3 = codigo_lote.endswith("-24")
    print(f"  ✓ Termina con '-24': {regla3}")
    
    # Para el octavo carácter primero nos aseguramos que el código sea lo suficientemente largo
    if len(codigo_lote) > 7:
        octavo_caracter = codigo_lote[7]
        regla4 = octavo_caracter in ['X', 'Y']
        print(f"  ✓ 8vo carácter es 'X' o 'Y': {regla4} (actual: '{octavo_caracter}')")
    else:
        regla4 = False
        print(f"  ✓ 8vo carácter es 'X' o 'Y': {regla4} (código muy corto)")
    
    # Si todas las reglas se cumplen, el código es válido
    es_valido = regla1 and regla2 and regla3 and regla4
    
    if es_valido:
        print(f"\n  ✅ Resultado: VÁLIDO")
    else:
        print(f"\n  ❌ Resultado: INVÁLIDO")
    
    return es_valido

# Probamos con los dos ejemplos que nos dieron
print("\n" + "-"*60)
validar_lote("LOT-45A-X-B-24")  # Este debería pasar todas las pruebas

print("\n" + "-"*60)
validar_lote("LOT-44B-Z-C-23")  # Este debería fallar algunas

print("\n" + "="*60)