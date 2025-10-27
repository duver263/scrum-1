# Experimentos exitosos registrados por cada equipo
equipo_A = {
    ("EXP-001", "2023-10-01"),
    ("EXP-002", "2023-10-02"),
    ("EXP-003", "2023-10-03")
}

equipo_B = {
    ("EXP-002", "2023-10-02"),
    ("EXP-004", "2023-10-04"),
    ("EXP-001", "2023-10-01")
}

# 1. Intersección → Experimentos reportados por ambos
interseccion = equipo_A & equipo_B

# 2. Unión → Total de experimentos exitosos únicos
union = equipo_A | equipo_B

# 3. Diferencia → Experimentos que solo hizo equipo_A
diferencia = equipo_A - equipo_B

# Imprimir resultados
print("Experimentos exitosos de ambos equipos (Intersección):")
print(interseccion)

print("\nTotal de experimentos exitosos únicos (Unión):")
print(union)

print("\nExperimentos realizados solo por equipo_A (Diferencia):")
print(diferencia)
