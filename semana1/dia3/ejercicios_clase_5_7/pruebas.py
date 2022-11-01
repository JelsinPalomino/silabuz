# Import library random
import random

# test
count = 0
num_inp = int(input("Ingrese el número: "))
num_rand = random.randint(1,1000)
print(num_rand)

while num_inp != num_rand:
    count +=1
    if num_inp > num_rand:
        print("El numero a adivinar ",num_rand ,"es menor que el número ingresado", num_inp)

    elif num_inp < num_rand:
        print("El numero a adivinar ",num_rand ,"es mayor que el número ingresado", num_inp)
    elif num_inp == num_rand:
        print("Adivinaste")
        break

    num_inp = int(input("Ingrese un número:"))

print("\n")
print("Adivinaste el numero en ", count, "intentos")    
