"""
Realizar un programa para que el usuario adivine un numero del 1 al 1000. Cada vez que el usuario 
escriba un numero le diras si el numero a adivinar es mayor o menor que el ingresado. Una vez que lo
adivine le indicaremos cuantas veces le tomo acertar.
"""

# Import library random
import random

# test
count = 0
number_input = int(input("Ingrese el número: "))
num_rand = random.randint(1,1000)
print(num_rand)

while number_input != num_rand:
    count +=1
    if number_input > num_rand:
        print(f"El numero a adivinar es menor que el número ingresado", number_input)

    elif number_input < num_rand:
        print(f"El numero a adivinar es mayor que el número ingresado", number_input)
    elif number_input == num_rand:
        print(f"Adivinaste - Felicitaciones!")
        break

    number_input = int(input(f"Ingrese un número:"))

print(f"\n")
print(f"Adivinaste el numero en ", count, "intentos")    



