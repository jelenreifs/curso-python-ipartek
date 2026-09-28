"""
Ejercicio 9 - Número mayor de una lista, sin max()
Dada la lista de números [14, 5, 20, 100, 2, 45], escribe un programa que recorra la lista y  encuentre el número más grande sin usar la función max(). 
"""
numeros = [14, 5, 20, 100, 2, 45]

# Partimos del primer elemento, no de 0: con una lista de
# negativos, empezar en 0 daría un resultado incorrecto
mayor = numeros[0]

for n in numeros:
    if n > mayor:  # noqa: PLR1730 - el enunciado pide no usar max()
        mayor = n

print(f"El número mayor es: {mayor}")