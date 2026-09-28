"""
Ejercicio 3 - Calculadora de descuentos
Una tienda ofrece descuentos según el monto de compra. 
• Menos de 100$: Sin descuento. 
• Entre 100$ y 500$: 5% de descuento. 
• Más de 500$: 10% de descuento. Escribe un script que calcule el precio final. 
"""

monto = float(input("Monto de la compra ($): "))

# El orden importa: se evalúa de arriba abajo y para en el primero
# que se cumple, así que no hace falta comprobar los dos extremos
if monto < 100:
    descuento = 0
elif monto <= 500:
    descuento = 0.05
else:
    descuento = 0.10

precio_final = monto * (1 - descuento)

print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Precio final: {precio_final:.2f}$")
