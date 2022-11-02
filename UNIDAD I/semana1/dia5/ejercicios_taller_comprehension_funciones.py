
# TALLER DE FUNCIONES -  DIA 5

"""
EJERCICIOS 01: 

teststring = "hola mundo, mi primera clase con listas de comprensión"

result = [1 if c==" " else 0 for c in teststring]
print(sum(result))


teststring = "hola mundo, mi primera clase con listas de comprensión"
result = [1 if c==" " else 0 for c in teststring]
print(result)



# EJERCICIO 02:

#1er metodo
l1 = [1,2,3,7]
l2 = [1,5,6,7]

l = [i for i in l1 for j in l2 if i==j]

print(l)

#2do metodo

# EJERCICIO 03
result = 0
result = [i for i in range(7,538) if "7" in str(i)]

print(result)

"""

# EJERCICIO 04
"""
dic = {k:v for k in range(10, 500+1) for v in list(str(k)) if int(v)!=0 and k % int(v)==0}
print(dic)
"""
#Ejercicio 05

"""
def extrae_column_n(M:list, n:int):
    list_value = []
    for i in M:
        list_value.append(i[n])
    return list_value

M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
n = 2

print(extrae_column_n(M,n))
"""

# EJERCICIO 06:

"""
Escribir una función encontrar_2 que reciba por parámetro dos
cadenas: cadena y subcadena. Retornar la posición de la 
subcadena si esta se encuentra dentro de la cadena y -1 
si no se encuentra. No usar find().

Ejemplo: si los argumentos son “abbbccda” y “bbc” entonces 
se retorna 2.

"""

def encontrar_2(cadena:str, subcadena:str):
    cont = 0
    if subcadena in cadena:
        for i in range(len(cadena)-1):
            if cadena[i:len(subcadena)-1]==subcadena:
                return i
    else:
        return -1
        
cadena = "abbbccda" 
subcadena = "bbc"

print(encontrar_2(cadena, subcadena))




    
