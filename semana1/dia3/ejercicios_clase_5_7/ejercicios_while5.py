"""
leer números enteros hasta que el usuario coloque el 0. luego indicar.
a. la suma de los números positivos.
b. la suma de los negativos.
c. la cantidad de números registrados

"""
from operator import truediv

number = int(input("Ingrese un Número Entero :\n"))
nPositivos = []
nNegativos = []
nRegistrados = []   # Registro, viene por paciente. 
ciclo = True
while ciclo == True :
    if number == 0:
        print("Salida")
        ciclo = False
    else :
        number = int(input("Ingrese un Número Entero :\n"))
        nRegistrados.append(number)
        if number >= 0:
            nPositivos.append(number)
        else :
            nNegativos.append(number)
print(f"Registrados: {len(nRegistrados)}")
print(f"Positivos: {nPositivos} Suma: {sum(nPositivos)}")
print(f"Negativos: {nNegativos} Suma: {sum(nNegativos)}")