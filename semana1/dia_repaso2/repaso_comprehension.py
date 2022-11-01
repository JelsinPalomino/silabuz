"""
1.- Crear una lista de numeros de 1 al 5

"""
"""
# primera forma
numeros = []
for n in range(1,6):
    numeros.append(n)
print(numeros)

# segunda forma

"""

"""
Actividad 01: Realizar una lista con el doble de los números del 1 al 10

"""
"""
doble = [n*2 for n in range(1,11)]
print(doble)
"""

"""
ACTIVIDAD 02: Crear una lista por comprensión , que contenga cinco 
cadenas de caracteres , con 1,2,3,4,5 asteriscos

"""
"""
cadena = ["*"*n for n in range(1,6)]
print(cadena)
"""
"""
ACTIVIDAD 03: Crear una lista con los números 2,3,5,8,9, crear una 
lista con el cuadrado de cada uno de los elementos de la lista de nombre número

"""
"""
numero = [2,3,5,8,9]
cuadrado = [n**2 for n in numero]
print(cuadrado)
"""
"""
ACTIVIDAD 04: Crear una lista con cada una de las letras guardadas en la variable cadena

"""
"""
cadena = "artefacto"
letras = [n for n in cadena]
print(letras)
"""

"""
ACTIVIDAD 05: desde una lista de nombre datos que contiene una serie de numeros, crear
una lista que solo contenga los numeros pares dentro de la lista dada.

"""
"""
datos = [14, 18, 24, 29, 36, 41, 85, 63, 74]

pares = [n for n in datos if n%2==0]
print(pares)
"""
"""
OTRO EJERCICIO:
"""
"""
pares = []
for i in range(1,6):
    for j in range(1,6):
        pares.append((i,j))
print(pares)
"""

pares = [(i,j) for i in range(1,6) for j in range(1,6) ]
print(pares)