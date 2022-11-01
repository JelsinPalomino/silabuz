"""
x = 10
y = 0

try:
    z = x/y
except Exception as ex:
    print("Ocurrión un problema de tipo", type(ex))
"""
"""
# DIFERENCIA ENTRE FUNCIONES Y GENERADORES
def funcion(coleccion):
    resultados = []
    for i in coleccion:
        if i %2 ==0:
            resultados.append(i*2)
        else:
            resultados.append(i+1)
    return resultados


def funcion_generadora(coleccion):
    for i in coleccion:
        if i %2 ==0:
            yield i*2
        else:
            yield i+1

import time
for valor_generado in funcion_generadora([1,2,3,4,5]):
    start = time.time()
    print(valor_generado)
    end = time.time()
    print(end - start)

print("\n")

for valor_generado in funcion([1,2,3,4,5]):
    start = time.time()
    print(valor_generado)
    end  = time.time()
    print(end-start)
"""
"""
input = "Humanidad"
chart = [c for c in input]
print(chart)
"""

input = 'A,B,C'
# delim = ','

x = input.split(',')
print(x)
