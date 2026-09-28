"""
Ejercicio 2 - Par o impar
Crea un programa que solicite un número entero al usuario y determine si es un número par  o impar. 
"""

numero = int(input("Introduce un número entero: "))

# El módulo % devuelve el resto. Si al dividir entre 2 el resto
# es 0, el número es par
if numero % 2 == 0:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")