"""Ejercicio 02 - Notación algorítmica


Calcula la hipotenusa de un triángulo rectángulo, conociendo sus catetos.
"""

# Bucle infinito: repite hasta que encuentre un break
while True:

    # input() siempre devuelve texto, así que el nombre no hay que convertirlo
    cateto1 = float(input("Longitud del primer cateto (cm): "))
    cateto2 = float(input("Longitud del segundo cateto (cm): "))

    # Verificamos que los catetos sean positivos
    if cateto1 <= 0 or cateto2 <= 0:
        print("Error: las longitudes de los catetos deben ser positivas.")
    else:
        # Calculamos la hipotenusa usando el teorema de Pitágoras
        hipotenusa = (cateto1**2 + cateto2**2)**0.5

        # :.2f formatea el número con 2 decimales
        print(f"La hipotenusa mide {hipotenusa:.2f} cm.")

    # Línea en blanco para separar visualmente cada cálculo
    print()
