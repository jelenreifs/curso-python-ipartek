"""
Ejercicio 1 - El recibo de la compra

Pide tres productos con su precio, calcula el subtotal, el IVA (21%)
y el total, y muestra el recibo.
"""

# --- Constante ---
# El tipo de IVA no cambia durante el programa: va en mayúsculas (PEP 8)
IVA = 0.21

# --- Entrada de datos ---
# input() devuelve siempre str, así que el nombre se guarda tal cual
producto1 = input("Producto 1: ")
precio1 = float(input("Precio: "))      # float: los precios llevan decimales

producto2 = input("Producto 2: ")
precio2 = float(input("Precio: "))

producto3 = input("Producto 3: ")
precio3 = float(input("Precio: "))

# --- Cálculos ---
subtotal = precio1 + precio2 + precio3

# round(numero, 2) redondea a 2 decimales y evita los errores típicos
# de los float: sin él, 1.20 + 0.90 + 3.50 puede dar 5.600000000000001
subtotal = round(subtotal, 2)

importe_iva = round(subtotal * IVA, 2)
total = round(subtotal + importe_iva, 2)

# --- Salida ---
print()
print("--- Recibo ---")
print(f"{producto1}: {precio1} €")
print(f"{producto2}: {precio2} €")
print(f"{producto3}: {precio3} €")
print(f"Subtotal: {subtotal} €")
print(f"IVA (21%): {importe_iva} €")
print(f"Total: {total} €")