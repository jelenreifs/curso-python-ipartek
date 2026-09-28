"""
Estructuras de datos - Ejercicio 5
Detectando anagramas

Pide dos cadenas y determina si son anagramas: mismas letras en distinto orden.
"""

# --- Entrada de datos ---
cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

# --- Proceso ---
# Normalizamos antes de comparar:
#   .lower()             -> "Roma" y "roma" deben contar igual
#   .replace(" ", "")    -> los espacios no son letras
limpia1 = cadena1.lower().replace(" ", "")
limpia2 = cadena2.lower().replace(" ", "")

# sorted() devuelve una LISTA con los caracteres ordenados
# alfabéticamente. Si dos palabras tienen las mismas letras,
# sus listas ordenadas son idénticas
if sorted(limpia1) == sorted(limpia2):
    print(f'"{cadena1}" y "{cadena2}" SÍ son anagramas.')
else:
    print(f'"{cadena1}" y "{cadena2}" NO son anagramas.')