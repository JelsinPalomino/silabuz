"""
Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , 
escriba un programa que pida al usuario una palabra, dicha palabra 
debe ser agregada al final y al inicio de la lista.
"""

lista =["Hola", "Amigos", "Hoy", True]
agregar=input('Ingrese un valor: ')
ubicacion=input('precione "I" si quiere que la lista es al inicio o "F" si quiere que este al final ').upper()
if ubicacion=='I':
      inicio=lista.insert(0,agregar)
else:      
      ultimo=lista.append(agregar)


print(lista)
