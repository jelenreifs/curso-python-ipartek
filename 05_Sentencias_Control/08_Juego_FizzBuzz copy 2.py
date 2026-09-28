"""
Ejercicio 8 - FizzBuzz
Imprime los números del 1 al 15. 
• Si el número es múltiplo de 3, imprime «Fizz». 
• Si es múltiplo de 5, imprime «Buzz». 
• Si es múltiplo de ambos (como el 15), imprime «FizzBuzz». 
• Si no, imprime el número. 
"""

for n in range(1, 16):
    # El caso de los dos múltiplos va PRIMERO: si no, el 15
    # entraría en la rama de Fizz y nunca llegaría aquí
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
