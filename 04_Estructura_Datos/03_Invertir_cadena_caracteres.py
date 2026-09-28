"""
Estructuras de datos - Ejercicio 3
Invertir cadena de caracteres

Pide una cadena y la muestra con los caracteres en orden inverso.
"""

# --- Entrada de datos ---
cadena = input("Introduce una cadena: ")

# --- Proceso ---
# Slicing con paso -1: recorre la cadena de atrás hacia delante.
# Al omitir inicio y fin, toma la cadena entera
invertida = cadena[::-1]

# --- Salida ---
print(f"Cadena original:  {cadena}")
print(f"Cadena invertida: {invertida}")