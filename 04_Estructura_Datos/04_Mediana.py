"""
Estructuras de datos - Ejercicio 4
Mediana de una lista

Calcula la mediana de una lista de enteros sin usar statistics.median().
Funciona para cualquier longitud, par o impar.
"""


def obt_mediana(lista):
    """Devuelve la mediana de una lista de números."""

    # sorted() devuelve una copia ordenada y NO toca la lista original.
    # Con lista.sort() modificaríamos la lista que nos han pasado
    ordenada = sorted(lista)
    n = len(ordenada)

    # // es división entera: descarta los decimales.
    # Para n=5 da 2, que es justo el índice central (0,1,[2],3,4)
    centro = n // 2

    # % es el resto: si al dividir entre 2 sobra algo, es impar
    if n % 2 == 1:
        # Impar: hay un único elemento central
        return ordenada[centro]
    else:
        # Par: la media de los dos centrales.
        # Para n=6, centro vale 3, así que los centrales son el 2 y el 3
        return (ordenada[centro - 1] + ordenada[centro]) / 2


# --- Programa principal ---
# La lista se inicializa aquí, no se pide al usuario
numeros = [7, 2, 9, 4, 1, 8, 5]

print(f"Lista original: {numeros}")
print(f"Lista ordenada: {sorted(numeros)}")
print(f"Mediana: {obt_mediana(numeros)}")