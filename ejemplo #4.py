# Lista de mediciones de diámetro (en mm)
mediciones = [10.01, 10.03, 9.98, 10.00, 10.05, 9.97]
diametro_objetivo = 10.0
tolerancia = 0.03 # +/-

piezas_aprobadas = 0
piezas_rechazadas = 0

# Bucle 'for' para iterar
for medicion in mediciones:
    diferencia = abs(medicion - diametro_objetivo)
    
    # Condicional 'if/elif/else'
    if diferencia <= tolerancia:
        print(f"Medición {medicion} mm: APROBADA")
        piezas_aprobadas += 1
    elif medicion < diametro_objetivo:
        print(f"Medición {medicion} mm: RECHAZADA (Muy pequeña)")
        piezas_rechazadas += 1
    else:
        print(f"Medición {medicion} mm: RECHAZADA (Muy grande)")
        piezas_rechazadas += 1

print(f"Total Aprobadas: {piezas_aprobadas} | Total Rechazadas: {piezas_rechazadas}")