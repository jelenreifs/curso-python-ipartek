"""
Ejercicio 2 - Conversor de temperatura

Pide una temperatura en grados Celsius y la convierte a Fahrenheit
y a Kelvin.
"""

# --- Entrada de datos ---
# float porque las temperaturas pueden llevar decimales (36.6)
celsius = float(input("Temperatura en Celsius: "))

# --- Cálculos ---
# Una variable por conversión: más legible que meter las fórmulas
# directamente dentro del print
fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

# --- Salida ---
# \n al principio produce la línea en blanco antes del resultado
# :g muestra el número sin ceros sobrantes: 100.0 se imprime como 100
print(f"\n{celsius:g} °C equivale a:")
print(f"   → {fahrenheit} °F")
print(f"   → {kelvin} K")
