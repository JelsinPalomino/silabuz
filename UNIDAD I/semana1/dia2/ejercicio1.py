# Ejercicio 1: Hacer un programa que pida al usuario 5 nombres. 
# Crear una lista con los 5 nombres. Despues hacer que muestre 
# una frase los pronombres que empiezan con la letra A

nombre = []
for i in range(0,5):
    name = input(str(i)+" Ingrese los nombres:")
    nombre.append(name)

for i in nombre:
    if i.startswith("a"):
        print("Todos ellos son amigos de", i)
    