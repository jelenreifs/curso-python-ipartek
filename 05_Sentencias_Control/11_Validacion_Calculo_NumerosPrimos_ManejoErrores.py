"""
Ejercicio 11 - Validación y cálculo de números primos en un rango con manejo  de errores
Este programa pide al usuario un rango numérico, valida que los datos sean correctos usando bucles while y excepciones, y encuentra todos los números primos dentro de ese  rango usando bucles for anidados y control de flujo (break/else). 
"""

# --- Entrada validada con while + try/except ---
# El bucle no sale hasta que el dato sea correcto
while True:
    try:
        inicio = int(input("Inicio del rango: "))
        fin = int(input("Fin del rango: "))
    except ValueError:
        # Salta si el usuario escribe letras en vez de números
        print("Error: introduce números enteros.")
        continue        # vuelve a pedir desde el principio

    if inicio < 2:
        print("Error: el inicio debe ser 2 o mayor (1 no es primo).")
    elif fin < inicio:
        print("Error: el final debe ser mayor o igual que el inicio.")
    else:
        break           # los datos son válidos, salimos del bucle

# --- Búsqueda de primos con for anidado ---
primos = []

for numero in range(inicio, fin + 1):

    # Solo hace falta probar divisores hasta la raíz cuadrada:
    # si n = a * b, uno de los dos es menor o igual que la raíz
    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            break       # divisor encontrado: NO es primo
    else:
        # El else del for solo se ejecuta si NO hubo break,
        # es decir, si no se encontró ningún divisor
        primos.append(numero)

# --- Salida ---
print(f"\nPrimos entre {inicio} y {fin}: {primos}")
print(f"Total encontrados: {len(primos)}")