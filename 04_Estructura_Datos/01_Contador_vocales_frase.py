"""
Estructuras de datos - Ejercicio 1
Contar vocales de una frase

Pide una frase y cuenta cuántas vocales contiene, tanto en
minúscula como en mayúscula.
"""

"""
Estructuras de datos - Ejercicio 1
Contar vocales de una frase (versión con lista)
"""

# --- Datos ---
# Lista de vocales en minúscula. Cada vocal es un elemento independiente
vocales = ["a", "e", "i", "o", "u"]

# --- Entrada de datos ---
frase = input("Introduce una frase: ")

# --- Proceso ---
contador = 0

for letra in frase.lower():
    # 'in' funciona igual sobre una lista que sobre una cadena:
    # comprueba si el elemento está dentro de la colección
    if letra in vocales:
        contador += 1

# --- Salida ---
print(f"\nFrase introducida: {frase}")
print(f"Resultado: {contador} vocales")