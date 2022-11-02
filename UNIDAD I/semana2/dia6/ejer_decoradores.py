"""
EJERCICIO 1:
Implementar la función get_avg que calcule el promedio de una lista de números:

def get_avg(lista):
  lista = [10, 40, 20, 45, 25, 35, 15]
  pass
La función get_avg retorna un float.

Asimismo implementar un decorador que permita imprimir los siguientes mensajes:

Inicio del cálculo del promedio de la lista de números.
El cálculo ha finalizado.
"""
"""
def decorador(funcParametro: ):
    def funcAuxiliar(*arg):
        print(f"Inicio del cálculo del promedio de la lista de números")
        n = funcParametro(*arg)
        return print(f"{n} \nEl calculo ha finalizado")
    return funcAuxiliar 

@decorador
def get_avg(lista):
  mean = sum(lista)/len(lista)
  return mean

listNum = [10, 40, 20, 45, 25, 35, 15]

get_avg(listNum)
"""

"""
#Natalia:
def decorador(func):
    def mensaje(*arg):
        print("Inicio del cálculo del promedio de la lista de números.") 
        n = func(*arg)
        return print(f"{n} \nEl cálculo ha finalizado")
    return mensaje

@decorador
def get_avg(lista)-> float:
    x = 0
    for num in lista:
        x += num
    return x/len(lista)

lista = [10, 40, 20, 45, 25, 35, 15]
get_avg(lista)
"""

"""
def get_avg(lista:float):
  lista = [10, 40, 20, 45, 25, 35, 15]
  pass
La función get_avg retorna un float.
"""
"""
EJERCICIO 2:
Escriba un programa que dada una entrada numérica por el usuario, ingrese a una 
función que duplique el valor y sea retornado en forma de string o cadena. 
Utilice tipos tanto para las variables como para las funciones.

"""
"""
def decorador(funcParametro):
    def funcAuxiliar(input):
        if type(input) != int :
            print("La operación no se puede realizar")
        else:
            print("Si se puede realizar")
        funcParametro(input)
        return 
    return funcAuxiliar

@decorador
def duplicate(input:int) -> str:
    n = str(input*2)
    return print(n)
    
input1 = int(input("Ingrese un numero: "))

duplicate(input1)


#:str
"""



"""
EJERCICIO 3:
Cree una función con anotaciones, que tome una palabra y duplique sus letras y las retorne en una lista.

Ejemplo:

Ingrese una palabra: hola

Retorna: ['h','h','o','o','l','l','a','a']
"""
def only_string(funcParametro):
    def funcAuxiliar(word):
        if type(word) == str:
            return funcParametro(word)
        else:
            return "Se necesita palabras y no numeros para realizar la operación"
    return funcAuxiliar

@only_string
def duplicate(word:str) -> str:
    duplicateWord = []
    for i in word:
        duplicateWord.append(str(i))
        duplicateWord.append(str(i))
    return duplicateWord

palabra = ""100""

print(duplicate(palabra))

"""
EJERCICIO 4:
Dada la función "calc_par_impar" que retorna un booleano, dependiendo si el número ingresado es par o impar, 
cree un decorador que imprima que tipo de número a recibido la función.

def calc_par_impar(n):
    if n % 2 == 0:
        return True
    return False

"""
"""
# 1ra_forma: 
def decorador(funcion) -> str:
    def funcion_auxiliar(n):
        if n %2 == 0:
            print(f"recibio un número par: {n}")
        else:
            print(f"recibio un número impar: {n}")
    return funcion_auxiliar

@decorador
def calc_par_impar(n):
    if n % 2 == 0:
        return True
    return False

print(calc_par_impar(3))
"""
"""
# 2da_forma:
def deco_tipo_de_numero(funcion):
    def fun_auxiliar(num):
        if num % 2==0:
            return funcion(True) 
        else:
            funcion(False)
    return fun_auxiliar

@deco_tipo_de_numero
def calc_par_impar(num):
    print(num)
calc_par_impar(5)
"""
"""
# 3ra_forma: 
def deco_tipo_de_numero(funcion)->bool:
    def fun_auxiliar(num:int):
        if num % 2==0:
            print('es par')
            return funcion(True) 
        else:
            print('es impar')
            funcion(False)
    return fun_auxiliar

@deco_tipo_de_numero
def calc_par_impar(num:int):
    return print(num)

calc_par_impar(7)

"""

"""
EJERCICIO 5:
Cree una función decoradora deco1 que muestre el siguiente flujo, para cualquier número ingresado, 
por ejemplo para el número 30:

- Hola, estoy decorando esta función.
- Ingresaste el número 30
- Terminé de decorar

def deco1(funcParametro):
  pass

@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)
"""
"""
# Maria
def deco1(funcion):
    def fun_auxiliar(num:int):
        print('Hola, estoy decorando esta función.')
        return funcion(num), print('Terminé de decorar')
    return fun_auxiliar

@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)
"""
"""
def deco1(funcParametro):
    def deco_aux(n: int):
        print('Hola, estoy decorando esta función.')
        return funcParametro(n), print('Terminé de decorar')
    return deco_aux

@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)
"""