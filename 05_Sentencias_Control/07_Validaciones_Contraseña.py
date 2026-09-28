"""
Ejercicio 7 - Validación de contraseña
Define una contraseña correcta en una variable (ej: «python123»). Pide al usuario que la  introduzca. Tiene 3 intentos. Si acierta, imprime «Acceso concedido». Si agota los intentos,  imprime «Cuenta bloqueada».
"""

CONTRASENA = "python123"
INTENTOS = 3

for intento in range(1, INTENTOS + 1):
    clave = input(f"Contraseña (intento {intento}/{INTENTOS}): ")

    if clave == CONTRASENA:
        print("Acceso concedido")
        break
else:
    # El else de un for se ejecuta SOLO si el bucle terminó
    # sin encontrarse ningún break
    print("Cuenta bloqueada")

