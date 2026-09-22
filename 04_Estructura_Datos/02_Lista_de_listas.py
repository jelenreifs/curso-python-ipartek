"""
Estructuras de datos - Ejercicio 2
Lista de listas (lista de dos dimensiones)
"""

# Lista de dos dimensiones: cada elemento es a su vez una lista
lis1 = [[4, 3, 5], [3, 5, 8], [4, 5, 6]]


def obt_valor_medio(lista):
    """Calcula el valor medio de todos los elementos de una lista 2D."""
    suma = 0
    cantidad = 0

    # Bucle anidado: el externo recorre las filas (cada sublista)
    # y el interno recorre los números dentro de cada fila
    for fila in lista:
        for numero in fila:
            suma += numero
            cantidad += 1      # contamos elementos, no filas

    # Devolvemos el resultado redondeado a 2 decimales
    return round(suma / cantidad, 2)


def obt_maximo(lista):
    """Devuelve el valor máximo de una lista 2D y su posición."""
    # Partimos del primer elemento como candidato inicial.
    # Empezar en 0 sería un error si la lista tuviera negativos
    maximo = lista[0][0]
    posicion = (0, 0)

    # enumerate() da el índice junto con el elemento
    for i, fila in enumerate(lista):
        for j, numero in enumerate(fila):
            if numero > maximo:
                maximo = numero
                posicion = (i, j)      # tupla (fila, columna)

    return maximo, posicion


# --- Programa principal ---
print(f"Lista: {lis1}")

media = obt_valor_medio(lis1)
print(f"Valor medio: {media}")

maximo, (fila, columna) = obt_maximo(lis1)
print(f"Valor máximo: {maximo}, en la fila {fila}, columna {columna}")