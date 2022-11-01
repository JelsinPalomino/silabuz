"""
En este ejercicio, ingrese con cajas enteras y displays con msgboxes, 
ambos pertenecientes al módulo easygui. Inicialice una lista con 5 números 
enteros de su elección y luego ingrese un número entero. En un bucle 
for, itere a través de la lista. Si el entero ingresado pertenece a la 
lista, guárdelo y rompe el ciclo (ya que lo encontraste). Si el ciclo 
terminó con éxito, use una cláusula else para mostrar un mensaje que lo 
anuncie. Ahora ingrese otro número entero, esta vez positivo. Escribe un 
bucle while para determinar si este entero es primo. si no lo es, el ciclo 
debe mostrar el primer divisor encontrado y terminar. Si es el primero, 
mostrarlo en una cláusula else.

"""
import easygui, sys

int_numbers = [5, 8 , 25 , 35, 38]

user_number = int(easygui.integerbox("Ingrese el número: "))

for i in int_numbers:
    if user_number == i:
        easygui.msgbox("Lo hallaste")
     



