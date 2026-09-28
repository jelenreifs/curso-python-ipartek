"""
Ejercicio 6 - Contador de vocales
Crea un programa que sume números introducidos por el usuario. El programa debe seguir  pidiendo números hasta que el usuario introduzca un 0. Al final, debe mostrar la suma total. 
"""

VOCALES = "aeiou"

frase = input("Introduce una frase: ")
contador = 0

# .lower() para que cuenten también las mayúsculas
for letra in frase.lower():
    if letra in VOCALES:
        contador += 1

print(f"La frase tiene {contador} vocales")
