"""
Ejercicio sobre archivo .csv con info de titanic
"""
"""
# Contar varones y mujeres del titanic
import csv
with open('E:/BACKEND/ejemplos/semana2/dia7/titanic.csv') as f:
    reader = csv.reader(f)
    
    # i[4]: para contar varones y mujeres
    datos = [i[4] for i in reader]
    f=[]
    m=[]
    for i in datos:
        if i=='male':
            m.append(i)
        elif i=='female':
            f.append(i)
    print(len(f),len(m))

"""
"""
# Promedio de la edad
import csv
with open('E:/BACKEND/ejemplos/semana2/dia7/titanic.csv') as f:
    reader = csv.reader(f)
    datos = [int(i[5]) for i in reader if i[5].isnumeric()]
    average = sum(datos)/len(datos)
    print(average)
"""
"""
import csv
with open('E:/BACKEND/ejemplos/semana2/dia7/titanic.csv') as f:
    reader = csv.reader(f)
    datos = [i for i in reader]
    print(datos[0])
"""

# TALLER EJERCICIO 4:


import csv
with open('E:\BACKEND\ejemplos\semana2\dia7\titanic.csv','r') as filetitanic :
    titanic = csv.reader(filetitanic)
    datos = []
    age = []
    sex = []
    survived = []
    for i in titanic:
        datos.append(i)

    for element in range(len(datos)):
        age.append(datos[element][5])
        sex.append(datos[element][4])
        survived.append(datos[element][1])

# Promedio de edades
    list_age = [int(i) for i in age if i.isnumeric()]
    print(f"""
Edades procesadas   :{len(list_age)}
Suma de edades      :{sum(list_age)}
#Promedio            :{sum(list_age)/len(list_age)}""")

# Numero de mujeres y hombre
    print(f"""
Numero de hombres : {sex.count('male')}
Numero de mujeres : {sex.count('female')}
""")

# Numeros de sobrevivientes y fallecidos
    print(f"""
Numero de Sobrevivientes : {survived.count('1')}
Numero de Fallecidos : {survived.count('0')}
""")