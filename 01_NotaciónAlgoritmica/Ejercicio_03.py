"""Ejercicio 03 - Notación algorítmica
Se desea tener un algoritmo que permita mostrar el nombre, el monto por
trabajar las horas normales, el monto por trabajar las horas extras, la
bonificación total por los hijos (por cada hijo se le da 5 soles) y finalmente el
pago total (es la suma del monto por pago de las horas normales, monto por
pago de las horas extras y la bonificación total por los hijos). Considere que
el pago por hora extra es 50% más del pago por hora normal.

Nombre
Total horas normales
Total horas extras
Bonificacíon total por hijos
Pago 50% más dle pago por hora normal
"""

# --- Constantes ---
# Se escriben en mayúsculas por convención (PEP 8): son valores fijos
BONO_POR_HIJO = 5
FACTOR_HORA_EXTRA = 1.5  # 50% más que la hora normal

# --- Entrada de datos ---
# input() siempre devuelve texto; hay que convertirlo para poder operar
nombre = input("Nombre del trabajador: ")
horas_normales = float(input("Horas normales trabajadas: "))
horas_extras = float(input("Horas extras trabajadas: "))
pago_por_hora = float(input("Pago por hora normal (S/.): "))
hijos = int(input("Número de hijos: "))  # int: los hijos no son decimales

# --- Cálculos ---
# Monto por las horas normales
monto_normal = horas_normales * pago_por_hora

# La hora extra se paga 1.5 veces la normal (el 100% + el 50% extra)
pago_hora_extra = pago_por_hora * FACTOR_HORA_EXTRA
monto_extra = horas_extras * pago_hora_extra

# 5 soles por cada hijo
bonificacion = hijos * BONO_POR_HIJO

# El pago total es la suma de los tres conceptos
pago_total = monto_normal + monto_extra + bonificacion

# --- Salida ---
print()  # línea en blanco para separar de las preguntas
print(f"Trabajador: {nombre}")
print(f"Monto por horas normales: S/. {monto_normal:.2f}")
print(f"Monto por horas extras:   S/. {monto_extra:.2f}")
print(f"Bonificación por hijos:   S/. {bonificacion:.2f}")
print(f"PAGO TOTAL:               S/. {pago_total:.2f}")
