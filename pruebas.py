import keyword

print(keyword.kwlist)

#  Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = True
# Si imprimir, print()
if imprimir:
    print(x, d)
# Salida: El valor de (a+b)*c es 14


def funcion(a, b, c):
    return a + b + c


d = funcion(10, 23, 3)
print(d)


# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10
