# bucle_for_basico1.py

# 1. Básico: imprime todos los números enteros del 0 al 100
# Bucle for con range de 0 a 100 (inclusive) - uso de bucle y función integrada range()
for i in range(101):
    print(i)  # Función integrada print()

# 2. Múltiples de 2 entre 2 y 500
# Bucle for con paso personalizado (range con 3 argumentos)
for i in range(2, 501, 2):
    print(i)

# 3. Contando Vanilla Ice: condicionales y operadores lógicos
for i in range(1, 101):  # Bucle for, range con inicio y fin
    if i % 10 == 0:  # Condicional if, operador módulo (divisible por 10)
        print("baby")  # Imprime cadena literal
    elif i % 5 == 0:  # Condicional elif, operador módulo (divisible por 5)
        print("ice ice")
    else:
        print(i)

# 4. Wow. Número gigante a la vista: acumulador y bucle con paso
suma_total = 0  # Declaración de variable (entero)
for i in range(0, 500001, 2):  # Bucle for con paso de 2 para números pares
    suma_total += i  # Acumulador - operador de asignación compuesta
print("Suma total de los pares de 0 a 500,000:", suma_total)  # Concatenación implícita con coma

# 5. Regrésame al 3: bucle regresivo
for i in range(2024, 0, -3):  # range con paso negativo para contar hacia atrás
    print(i)

# 6. Contador dinámico: uso de múltiples variables y condicionales
numInicial = 3  # Declaración de variable
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):  # Bucle con límites variables
    if i % multiplo == 0:  # Condicional + operador módulo
        print(i)
