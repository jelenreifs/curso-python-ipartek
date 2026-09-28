"""
Ejercicio 5 - Sumatoria de números
Crea un programa que sume números introducidos por el usuario. El programa debe seguir  pidiendo números hasta que el usuario introduzca un 0. Al final, debe mostrar la suma total. 

"""

suma = 0

while True:
    n = int(input("Número (0 para terminar): "))
    if n == 0:
        break
    suma += n

print(f"Suma total: {suma}")