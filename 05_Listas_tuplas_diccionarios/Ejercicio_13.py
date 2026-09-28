"""
Ejercicio 13 - Clase SecuenciaAritmetica

Iterador completo de una secuencia aritmética: valor inicial,
paso constante y número máximo de términos.

-----------------------------------------------------------------------
# Al crear:
#   - comprobar paso != 0 y terminos > 0, si no lanzar error
#   - guardar la configuración: inicio, paso, terminos
#   - preparar el estado: actual = inicio, restantes = terminos
#
# Al empezar a iterar (__iter__):
#   - devolver el estado a su valor de partida
#   - devolverme a mí misma
#
# En cada paso (__next__):
#   - si no quedan términos, parar
#   - guardar el valor actual, avanzar, descontar uno, devolver el guardado
#
# __len__: cuántos quedan
# __str__: la secuencia entera, SIN tocar el estado
"""


class SecuenciaAritmetica:
    """Genera una secuencia aritmética recorrible las veces que haga falta."""

    def __init__(self, inicio, paso, terminos):
        # --- Validaciones ---
        # Con paso 0 la secuencia nunca avanzaría: siempre el mismo valor
        if paso == 0:
            raise ValueError("El paso no puede ser 0")
        if terminos <= 0:
            raise ValueError("El número de términos debe ser positivo")

        # --- Configuración (no cambia nunca) ---
        self.__inicio = inicio
        self.__paso = paso
        self.__terminos = terminos

        # --- Estado (va cambiando al recorrer) ---
        # Se inicializa aquí para que next() funcione sin llamar antes a iter()
        self.__actual = inicio
        self.__restantes = terminos

    def __iter__(self):
        """Devuelve el iterador, reiniciando el estado."""
        # Esta es la clave: reiniciar aquí permite recorrer la secuencia
        # varias veces. Sin esto, el segundo list() devolvería []
        self.__actual = self.__inicio
        self.__restantes = self.__terminos
        return self

    def __next__(self):
        """Devuelve el siguiente término, o para la iteración si no quedan."""
        if self.__restantes == 0:
            raise StopIteration

        valor = self.__actual           # guardamos el valor a devolver
        self.__actual += self.__paso    # preparamos el siguiente
        self.__restantes -= 1           # un término menos por delante
        return valor

    def __len__(self):
        """Número de términos que quedan por recorrer."""
        return self.__restantes

    def __str__(self):
        """Secuencia completa, sin tocar el estado del iterador."""
        # Calculamos los valores aparte, a partir de la configuración.
        # Si iteráramos self, __str__ consumiría o reiniciaría la secuencia
        valores = [self.__inicio + self.__paso * i
                   for i in range(self.__terminos)]
        return " → ".join(str(v) for v in valores)


# ============================================================
# Pruebas
# ============================================================

seq = SecuenciaAritmetica(2, 3, 5)
print("Secuencia(2, paso=3, términos=5):")

# for llama a __iter__ (reinicia) y luego a __next__ repetidamente
print("  for:", end=" ")
for valor in seq:
    print(valor, end=" ")
print()

# list() y sum() también llaman a __iter__, así que cada uno
# empieza desde el principio
print("  list:", list(seq))
print("  sum:", sum(seq))
print("  str:", seq)          # print() usa __str__ automáticamente

# Paso negativo: la secuencia decrece
seq2 = SecuenciaAritmetica(10, -2, 6)
print("\nSecuencia(10, paso=-2, términos=6):")
print("  for:", end=" ")
for valor in seq2:
    print(valor, end=" ")
print()

# Paso decimal
seq3 = SecuenciaAritmetica(0, 0.5, 8)
print("\nSecuencia(0, paso=0.5, términos=8):")
print("  for:", end=" ")
for valor in seq3:
    print(valor, end=" ")
print()

# next() directo, sin for
seq4 = SecuenciaAritmetica(1, 1, 3)
print("\nnext() directo:", next(seq4), next(seq4), next(seq4))

# len() devuelve los términos que quedan
seq5 = SecuenciaAritmetica(1, 1, 5)
iter(seq5)                    # reinicia el estado
next(seq5)
print(f"len() tras un next(): {len(seq5)}")     # 4

# Validación
print("\nError esperado:", end=" ")
try:
    SecuenciaAritmetica(1, 0, 5)
except ValueError as e:
    print(e)