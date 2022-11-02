"""
CSES - Weird Algorithm

Consider an algorithm that takes as input a positive integer n. 
If n is even, the algorithm divides it by two, and if n is odd, 
the algorithm multiplies it by three and adds one. The algorithm 
repeats this, until n is one. For example, the sequence for n=3 is as follows:

3→10→5→16→8→4→2→1

Your task is to simulate the execution of the algorithm for a 
given value of n.

"""

# Validación de numeros positivos
"""
number_input = int(input("Ingrese un número: "))
control = False

while number_input != 1: 
    if number_input % 2 ==0:
        new_number = number_input/2
        print(new_number)
    else:
        new_number = (number_input*3)+1
        print(new_number)
    number_input = new_number

    print(new_number, end="->", flush=True)
"""

while True:
    try:
        num = abs(int(input("Ingrese un número: ")))
        print(num, end = "")
        break
    except ValueError:
        print("Ingrese un número entero")
    continue
while num != 1: 
    if num % 2 == 0:
        num //= 2
    else:
        num = (num * 3) + 1
    print(f' {num}', end = '')