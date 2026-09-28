"""
Ejercicio 10 - Menú de opciones
Crea un menú interactivo que se repita hasta que el usuario elija salir. 
1. Saludar 
2. Sumar dos números 
3. Salir 
"""
while True:
    print("\n--- MENÚ ---")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"¡Hola, {nombre}!")

    elif opcion == "2":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"{a} + {b} = {a + b}")

    elif opcion == "3":
        print("Hasta luego.")
        break

    else:
        print("Opción no válida. Introduce 1, 2 o 3.")