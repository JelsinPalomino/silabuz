"""
PREGUNTA 1:
Dada la lista de notas [15,20,18] y 
la lista de alumnos ["Marcelo", "José", "Juan"] 
Imprimirlos de la siguiente forma:

Marcelo : 15
José : 20
Juan : 18

"""

"""
notas = [15,20,18]
alumnos = ["Marcelo", "José", "Juan"]
for alumnos, notas in zip(alumnos, notas):
    print(f'{alumnos} : {notas} ')
"""

"""
PREGUNTA 2:
Dada la siguiente lista ['Hola', True, 5, 6.04]
Imprimir los valores e índices sin utilizar un contador o range.

0 -> Hola
1 -> True
2 -> 5
3 -> 6.04

"""

"""
lista = ['Hola', True, 5, 6.04]

for cont,value in enumerate(lista):
    print(f"{cont} -> {value}")
"""

"""
PREGUNTA 3:
Dada la lista de notas [15,20,18] y 
la lista de alumnos ["Marcelo", "José", "Juan"], imprimirlos de la siguiente forma:

1 -> Jose : 20
2 -> Juan : 18
3 -> Marcelo : 15

No usar range, ni comparadores. Hint: usar sorted

"""

"""
lista_notas = [15,20,18]
lista_alumnos = ["Marcelo", "José", "Juan"]

lista = list(zip(lista_alumnos,lista_notas))

for count, value in enumerate(lista):
    value = sorted(lista)
    # print(count,"->",value[count][0],":",value[count][1])
    print(f"{count} -> {value[count][0]} : {value[count][1]}")
"""

"""
PREGUNTA 4:
Escriba un generador que permita contar las letras de las palabras de una lista.
Ejemplos:

Para "humanidad": {'h': 1, 'u': 1, 'm': 1, 'a': 2, 'n': 1, 'i': 1, 'd': 2}

Para "humano": {'h': 1, 'u': 1, 'm': 1, 'a': 1, 'n': 1, 'o': 1}

"""
"""
# 1ra forma: 

lista1 = ["humanidad", "humano", "desoxirribonucleico"]

def counts_letters(lista1):
    for word in lista1:
        contador = {}
        for c in word:
            if c not in contador:
                contador[c]=0
            contador[c] +=1
        yield contador

for n in counts_letters(lista1):
    print(n)
"""
"""
# 1.1 forma_prueba

#palabra = ["humanidad","humano"]
palabra='desoxirribonucleico'

def pregunta4(palabra):
    new_list={l:palabra.count(l) for l in palabra}
    yield new_list

for n in pregunta4(palabra):
    print(n)
"""
"""
#2da forma:
palabra='humanidad'

def pregunta4():
    new_list={l:palabra.count(l) for l in palabra}
    yield new_list

for n in pregunta4():
    print(n)
"""
"""
3ra forma:
palabra='carro'

def pregunta4():
    new_list={l:palabra.count(l) for l in palabra}
    yield new_list
ejemplo=pregunta4()
for n in ejemplo:
    print(n)
"""

"""
PREGUNTA 5:
Teniéndos los siguientes criterios:

Desaprobado: nota < 11
Destacado: nota > 16
Aprobado: para el resto de casos

notas = [15, 20 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)

def registrar_aprobados(l):
    pass
Implementar registrar_aprobados como generador y que su único parametro de entrada sea alumnos_notas. Posteriormente0 
utilizar un bucle y enumerate para obtener la siguiente salida.

1 -> Marcelo : 15 (Aprobado)
2 -> Jose : 20 (Destacado)
3 -> Juan : 18 (Destacado)
4 -> Marco : 11 (Aprobado)
5 -> María : 4 (Desaprobado)
6 -> Ricardo : 7 (Desaprobado)
7 -> Liz : 14 (Aprobado)
8 -> Diego : 13 (Aprobado)
9 -> Roberto : 1 (Desaprobado)
10 -> Martin : 9 (Desaprobado)
11 -> Álvaro : 10 (Desaprobado)

"""
"""
# 1ra forma
grades   = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
students = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]

def registrar_aprobados(gradSt):
    for grades, students in gradSt:
        if grades < 11:
            yield str(grades) + " (Desaprobado)", students
        elif grades > 16: 
            yield str(grades) + " (Destacado)", students
        else:
            yield str(grades) + " (Aprobado)", students 

for cont,(v1, v2) in enumerate(registrar_aprobados(zip(grades, students)), start = 1):
    print(f"{cont} -> {v2} : {v1}")
"""

# 2da forma
grades   = [15, 20, 18, 11, 4, 7, 14, 13 ,1 ,9, 10]
students = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]

def registrar_aprobados(gradSt):
    for grades, students in gradSt:
        if grades < 11:
            yield str(grades) + " (Desaprobado)", students
        elif grades > 16: 
            yield str(grades) + " (Destacado)", students
        else:
            yield str(grades) + " (Aprobado)", students 

for cont,(v1, v2) in enumerate(registrar_aprobados(zip(grades, students)), start = 1):
    print(f"{cont} -> {v2} : {v1}")
