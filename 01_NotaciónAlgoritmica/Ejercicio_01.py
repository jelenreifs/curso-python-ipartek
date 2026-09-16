"""
Ejercicio 01 - Notación algorítmica

Calcular la nota final de cada alumno según el siguiente criterio:
la parte práctica vale el 10%, la parte de problemas el 50% y la
parte teórica el 40%.

El algoritmo leerá el nombre del alumno y las tres notas, y escribirá
el resultado. Las notas deben estar entre 0 y 10; si no lo están, no
imprimirá las notas, mostrará un mensaje de error y volverá a pedir
otro alumno.
"""

"""
Ejercicio 01 - Notación algorítmica

Calcula la nota final de cada alumno: prácticas 10%, problemas 50%,
teoría 40%. Las notas deben estar entre 0 y 10; si no, muestra un
error y pasa al siguiente alumno.
"""

# Bucle infinito: repite hasta que encuentre un break
while True:

# input() siempre devuelve texto, así que el nombre no hay que convertirlo
    nombre = input("Nombre del alumno (Intro para salir): ")

    # Si el usuario pulsa Intro sin escribir nada, salimos del bucle
    if nombre == "":
        print("Fin del programa.")
        break

    # float() convierte el texto a número decimal
    practica = float(input("Nota de prácticas (0-10): "))
    problemas = float(input("Nota de problemas (0-10): "))
    teorica = float(input("Nota teórica (0-10): "))

    # Basta con que UNA nota esté fuera de rango para que sea inválida,
    # por eso se usa 'or': si alguna condición se cumple, entra aquí
    if practica < 0 or practica > 10 or problemas < 0 or problemas > 10 or teorica < 0 or teorica > 10:
        print("Error: las notas deben estar entre 0 y 10.")
    else:
        # Solo llega aquí si las tres notas son válidas
        nota_final = practica * 0.1 + problemas * 0.5 + teorica * 0.4

        # :.2f formatea el número con 2 decimales
        print(f"{nombre}: nota final = {nota_final:.2f}")

    # Línea en blanco para separar visualmente cada alumno
    print()

