# funciones_intermedias_1.py

# 1. Actualizar valores en diccionarios y listas

# Cambiar valor en matriz
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6  # Cambia el 3 por 6
# Resultado esperado: [[10, 15, 20], [6, 7, 14]]

# Cambiar nombre del primer cantante
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"

# Cambiar Cancún por Monterrey
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"

# Cambiar latitud en coordenadas
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios

def iterarDiccionario(lista):
    for diccionario in lista:
        # BONUS: formato mejorado
        salida = []
        for clave, valor in diccionario.items():
            salida.append(f"{clave} - {valor}")
        print(", ".join(salida))

# 3. Obtener valores de una lista de diccionarios

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

# 4. Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave in diccionario:
        valores = diccionario[clave]
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print(valor)

# Pruebas (puedes comentar estas antes de entregar si el sistema lo requiere)

# Prueba para iterarDiccionario
cantantes_test = [
    {"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

# iterarDiccionario(cantantes_test)

# Prueba para iterarDiccionario2
# iterarDiccionario2("nombre", cantantes_test)
# iterarDiccionario2("pais", cantantes_test)

# Prueba para imprimirInformacion
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

# imprimirInformacion(costa_rica)
