"""
Ejercicio 12 - Simulador de cajero automático con control de intentos y transacciones 
Este algoritmo simula un control de acceso por PIN con un límite de 3 intentos fallidos (bloqueando el sistema)
Tiene que contenerun menú interactivo con bucle while para realizar operaciones de  saldo, depósitos y retiros con validaciones estrictas.
"""

# --- Configuración ---
PIN_CORRECTO = "1234"
MAX_INTENTOS = 3

saldo = 1000.0

# Variable bandera: guarda si el usuario ha acertado el PIN.
# Empieza en False y solo pasa a True si acierta
acceso_concedido = False

# --- Control de acceso ---
for intento in range(1, MAX_INTENTOS + 1):
    pin = input(f"Introduce tu PIN ({intento}/{MAX_INTENTOS}): ")

    if pin == PIN_CORRECTO:
        print("PIN correcto. Bienvenida.")
        acceso_concedido = True
        break

    restantes = MAX_INTENTOS - intento
    if restantes > 0:
        print(f"PIN incorrecto. Te quedan {restantes} intentos.")

# --- Menú de operaciones ---
# Todo el menú queda DENTRO de este if: si no hubo acceso,
# el programa se salta el bloque entero y termina solo
if not acceso_concedido:
    print("Tarjeta bloqueada. Contacte con su oficina.")
else:
    while True:
        print("\n--- CAJERO ---")
        print("1. Consultar saldo")
        print("2. Ingresar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Operación: ")

        if opcion == "1":
            print(f"Saldo disponible: {saldo:.2f} €")

        elif opcion == "2":
            try:
                cantidad = float(input("Cantidad a ingresar: "))
            except ValueError:
                print("Error: introduce una cantidad numérica.")
                continue

            # Validación: no tiene sentido ingresar cero o negativo
            if cantidad <= 0:
                print("Error: la cantidad debe ser positiva.")
            else:
                saldo += cantidad
                print(f"Ingreso realizado. Nuevo saldo: {saldo:.2f} €")

        elif opcion == "3":
            try:
                cantidad = float(input("Cantidad a retirar: "))
            except ValueError:
                print("Error: introduce una cantidad numérica.")
                continue

            if cantidad <= 0:
                print("Error: la cantidad debe ser positiva.")
            elif cantidad > saldo:
                # Validación estricta: no permitir números rojos
                print(f"Saldo insuficiente. Disponible: {saldo:.2f} €")
            else:
                saldo -= cantidad
                print(f"Retire su dinero. Nuevo saldo: {saldo:.2f} €")

        elif opcion == "4":
            print("Gracias por usar el cajero.")
            break

        else:
            print("Opción no válida.")