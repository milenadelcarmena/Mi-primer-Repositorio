# Datos de temperaturas en formato [ciudades][días de la semana][semanas]
temperaturas = [
    [  # Ciudad 1: "Ciudad A"
        [25, 27, 26, 24, 30, 29, 28],  # Semana 1
        [26, 28, 29, 25, 31, 27, 24],  # Semana 2
        [24, 26, 28, 29, 30, 28, 27],  # Semana 3
        [30, 29, 28, 27, 26, 25, 24]  # Semana 4
    ],
    [  # Ciudad 2: "Ciudad B"
        [31, 30, 29, 32, 28, 29, 27],  # Semana 1
        [29, 28, 27, 30, 31, 32, 33],  # Semana 2
        [27, 26, 29, 30, 31, 28, 30],  # Semana 3
        [32, 31, 30, 29, 28, 27, 26]  # Semana 4
    ]
]

# Inicializar listas para promedios
promedios = []

# Iterar sobre las ciudades
for ciudad in range(len(temperaturas)):
    suma_semanas = []
    # Iterar sobre las semanas
    for semana in range(len(temperaturas[ciudad])):
        suma_temperaturas = sum(temperaturas[ciudad][semana])  # Sumar las temperaturas de la semana
        promedio = suma_temperaturas / len(temperaturas[ciudad][semana])  # Calcular promedio
        suma_semanas.append(promedio)  # Guardar el promedio por semana

    promedios.append(suma_semanas)  # Guardar promedios de la ciudad

# Mostrar resultados
for i in range(len(promedios)):
    print(f"Promedios para Ciudad {i + 1}: {promedios[i]}")
