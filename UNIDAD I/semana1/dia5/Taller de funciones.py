print("""
Ejercicio 1
Contar el número de espacios en un string dado.
count_string("Esta cadena tiene 4 espacios")
""")

print("Forma 01")
def count_string(string):
    count_space =  string.count(" ")
    print(f"Espacios en cadena: {count_space}")


count_string("Esta cadena tiene 4 espacios")

print("Forma 02")
def count_string_02(string):
    space = [i for i in string if " " in i]
    count_space = len(space)
    #nombres = [nombre.capitalize() if nombre is not None else "" for nombre in lista]
    print(f"Espacios en cadena Forma 2: {count_space}")

count_string_02("Esta cadena tiene 4 espacios")



print("""
Ejercicio 2
Plantear 2 formas de encontrar los números comunes entre 2 listas sin usar set.
""")
list_1 = [i*2 for i in range(0,15)]
list_2 = [i*4 for i in range(0,15)]
list_3 = []
print(list_1, list_2)

print("Forma 01")
def common_num(list01,list02):
    common_list = []
    for num in list_1:
        if num in list_2:
            common_list.append(num)
    print(common_list)

common_num(list_1,list_2)

print("Forma 02")

def common_num_02(list01,list02):
    common_list= [num for num in list01 if num in list02]
    print(common_list)

common_num_02(list_1,list_2)

print("""
Ejercicio 3
Encontrar todos los números comprendidos entre 7 y 537 que contengan el dígito 7
""")
list_numbers = [i for i in range(7,38)]
print(list_numbers)

def search_7(numbers):
    search_list = [i for i in numbers if "7" in str(i)]
    print(search_list)

search_7(list_numbers)

print(
    """
Ejercicio 4
Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo dígito
más alto por el cuál es divisible. Por ejemplo para 328 es 8.
    """
)

dic = {k:v for k in range(10,501) for v in list(str(k)) if int(v) !=0 and k % int(v) ==0}
print(dic)

print(
    """
Escribir una función extrae_columna_n que reciba como parámetro una lista M y un valor n.
La función debe extraer los valores "de la columna" n específica a la lista anidada dada.
La función debe verificar que n esté en el rango permitido. Caso contrario,
la función debe retornar una lista vacía.

Ejemplo:

M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

n = 0

Para extrae_column_n(M, n) la función retornará [1, 2, 1]
    """
)
def extrae_columna_n(M:list,n:list):
    list_value = []
    list_value=[i[n]for i in M]
    return print(list_value)

M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

n = 0
extrae_columna_n(M,n)

print(
    """
Ejercicio 6
Escribir una función encontrar_2 que reciba por parámetro dos cadenas:
cadena y subcadena. Retornar la posición de la subcadena si esta se encuentra
dentro de la cadena y -1 si no se encuentra. No usar find().
Ejemplo: si los argumentos son “abbbccda” y “bbc” entonces se retorna 2.
    """
)

cadena = "abbbccda"
subcadena = "bbc"

def encontrar_2(cad,subcad):
    if subcad in cad:
        print(cad.index(subcad))
    else :
        print(-1)
encontrar_2(cadena,subcadena)

print("""
Ejercicio 7
Escribir una función imprime_lista_anidada_1 para imprimir listas anidadas.
Cada sublista debe ser impresa en una línea diferente. Los elementos dentro
de la sublista deben estar separados por una tabulación. No use índices.
Si el argumento es [[1,2,3],[4,5],[6,7,8,9]], la función debe imprimir:

1 2 3 4 5 6 7 8 9
""")
lista = [[1,2,3],[4,5],[6,7,8,9]]
def imprime_lista_anidada_1(list):
    for i in list:
        print(*i, end="  ")

imprime_lista_anidada_1(lista)

print("""
Ejercicio 8
Escribir una función contador_elementos_lista que reciba como parámetro una
lista anidada L de números y un número n. La función cuenta el número de
listas anidadas que contienen un elemento en particular.

Plantee 2 formas de solución.

Ejemplo 1:

L = [[1, 3], [5, 7], [1, 11], [1, 15, 7], [5, 6, 21]] n = 1 Entonces la función retornará 3.

Ejemplo 2:

L = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']] n = ’B’ Entonces la función retornará 2.
""")
L =[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
n = "B"
print("Forma 01")
def contador_elementos_lista(l,n):
    contador = []
    for i in l:
        if n in i:
            contador.append(i)
    return print(len(contador))
contador_elementos_lista(L,n)

print("Forma 02")
def contador_elementos_lista_2(l,n):
    contador = [i for i in l if n in i]
    return print(len(contador))
contador_elementos_lista_2(L,n)

print("""
Ejercicio 9
Escribir una función elimina_duplicados que reciba como parámetro una
lista L y retorne una nueva lista sin los elementos duplicados.
Si el argumento es [500,100,200,300,200,100,600,400,800,400,500,900]
la función devuelve [500, 100, 200, 300, 600, 400, 800, 900]

Plantee 2 formas de solución
""")
L = [500,100,200,300,200,100,600,400,800,400,500,900]
def elimina_duplicados(l):
    not_duplicated = set()
    for i in l:
        not_duplicated.add(i)
    return print(not_duplicated)
print("Forma 01")
elimina_duplicados(L)

def elimina_duplicados_2(l):
    not_duplicated = set(i for i in l)
    return print(not_duplicated)
print("Forma 02")
elimina_duplicados_2(L)

print("""
Ejercicio 10
Implementar la serie de fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    """)
