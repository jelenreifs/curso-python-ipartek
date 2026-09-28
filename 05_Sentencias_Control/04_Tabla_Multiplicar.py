"""
Ejercicio 4 - Tabla de multiplicar
Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10 usando un 
"""

numero = int(input("Número para la tabla: "))

for i in range(1, 11):          # el 11 no se incluye
    print(f"{numero} x {i} = {numero * i}")
