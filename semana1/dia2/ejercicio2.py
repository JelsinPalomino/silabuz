"""
Ejercicio 2: Haga un programa en Python que le pida al
usuario tantos enteros como quiera, luego cree dos listas,
 una con la lista de números propuestos y la otra con
el número de ocurrencias. Por ejemplo, si el usuario ingresa
4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2]
"""
import random

num = int(input("¿Cuántos valores va a agregar?: "))
list_01 = []
list_02 = []
list_03 = []
for i in range(num):
    value = int(input("Ingrese el valor entero: "))
    list_01.append(value)
for j in range(int(num/2+1)):
    value = random.randint(0, 11)
    list_02.append(value)
for k in range(int(num/2+1)):
    n = random.randint(0,num)
    list_03.append(list_01[n])

print(list_03)
