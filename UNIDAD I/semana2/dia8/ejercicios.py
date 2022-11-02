"""
PREGUNTA 1.

Escriba un programa en Python que acepte el perímetro de un círculo que escriba un usuario.

Finalmente el programa debe imprimir:

El valor de π con 7 decimales.
El valor del área de dicho círculo (con 3 decimales) así como el valor del radio de dicho círculo (con 2 decimales).
Pistas

En geometría, el área encerrada por un círculo de radio r es π*r^2.
Del módulo math obtenga el valor de π para los cálculos que requiera.
La letra griega π representa una constante, que es igual a la relación entre la circunferencia de cualquier círculo y su diámetro.
"""
"""
import math
radio = 5
pi= round(math.pi,7)
areac = round(pi * (radio**2),2)
print(areac)
"""

import math
perimetro = 15.5
radio = round(perimetro/2,2)
pi= round(math.pi,7)
areac = round(pi * (radio**2),3)
#print(f"""
#Perimetro   :{perimetro}
#π           :{pi}
#Radio       :{radio}
#Area        :{areac}""")

"""
PREGUNTA 2
El presente ejercicio se enfoca en la manipulación de fechas utilizando datetime (Documentación oficial)

Explore la documentación y escriba un programa Python para mostrar la fecha 
y la hora actuales bajo los siguientes formatos de ejemplo (imaginando hoy fuese 10 de septiembre del 2022):

10-09-22
10-09-2022
Hoy día es Saturday
10~09~2022
10-09-2022 14:20:51
En caso obtengan Hoy día es Sábado no habría problema alguno, no se evaluará lo referente a los idiomas.

Es importante mencionar que la exploración de la documentación es importante 
sobretodo cuando le toque explorar de un paquete que no sea popular
"""
# Revisar la documentación
"""
import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES')

import datetime
day=datetime.datetime.now()
print(day.strftime("%d-%m-%y"))
print(day.strftime("%d-%m-%Y"))
print(f'Hoy dia es {day.strftime("%A")}')
print(day.strftime("%d~%m~%Y"))
print(day.strftime("%d-%m-%Y %H:%M:%S"))

"""
"""
PREGUNTA 3
Escriba un programa de Python para listar todos los archivos en un directorio en Python. 
(por precaución que sea en una carpeta temporal y que no contenga archivos importantes, coloque copias)

"""
"""
import pathlib

# Creen una carpeta cualquiera y agreguen archivos de diversas extensiones

direct_music = 'E:\BACKEND\ejemplos\semana2\dia8\pruebas'
directM      = pathlib.Path(direct_music)

for file in directM.iterdir():
    print(file.name)

"""
"""
PREGUNTA 4
Sin usar bibliotecas como pandas.

Generar un archivo local con el contenido del siguiente archivo:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Utilizando import csv

Calcular:

El promedio de edad.
La distribución del sexo (número de mujeres vs varones).
El número de sobrevivientes y fallecidos.

"""

# EN ARCHIVO PRUEBAS

"""
PREGUNTA 5
Escriba un programa en Python para calcular el número de días entre dos 
fechas. No es necesario que use inputs para el ingreso de las fechas.

"""
"""
from datetime import datetime
import datetime

firstD  = datetime.date(2022, 12, 1)
secondD = datetime.date(2022, 12, 12)
daysD   = secondD - firstD
print(daysD.days)
"""
"""
PREGUNTA 6:
Crear el archivo ejemplo.csv copiando el contenido del siguiente archivo: https://pastebin.com/gumjjcpx

QuotaAmount,StartDate,OwnerName,Username
150000,2016-01-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
167400,2016-02-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
155000,2016-03-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
132000,2016-01-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
200000,2016-02-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
180000,2016-03-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
110000,2016-01-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
100000,2016-02-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
145000,2016-03-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
135000,2016-01-01,Catherine Brown,trailhead16.kojyepokybge@example.com
145000,2016-02-01,Catherine Brown,trailhead16.kojyepokybge@example.com
180000,2016-03-01,Catherine Brown,trailhead16.kojyepokybge@example.com
190000,2016-01-01,Kelly Frazier,trailhead7.zdcsy4ax10mr@example.com
200000,2016-02-01,Kelly Frazier,trailhead7.zdcsy4ax10mr@example.com
100000,2016-03-01,Kelly Frazier,trailhead7.zdcsy4ax10mr@example.com
110000,2016-01-01,Dennis Howard,trailhead4.wfokpckfroxp@example.com
115000,2016-02-01,Dennis Howard,trailhead4.wfokpckfroxp@example.com
125000,2016-03-01,Dennis Howard,trailhead4.wfokpckfroxp@example.com

Desarrolle un función que lea el archivo y que de la columna QuotaAmount, calcule el 
promedio de los valores para luego retornarlo.

"""
"""

# 1ra forma con la cual estamos haciendo el unittest:
import csv
def averageCsv():
    with open("pregunta6.csv") as f:
        read = csv.reader(f)
        datos = [int(i[0]) for i in read if i[0].isnumeric()]
        average = sum(datos)/len(datos)
        print(average)
    return average

averageCsv()


import csv
def first_term():
    with open("pregunta6.csv") as f:
        read = csv.reader(f)
        datos = [int(i[0]) for i in read if i[0].isnumeric()]
        print(datos[0])

first_term()
"""
"""
#2da forma 
import csv
def ReadFile():
    with open('pregunta6.csv','r') as f :
        ejemplo = csv.reader(f)
        datos=[]
        promedio=[]
        for i in ejemplo:
            if i[0]!='QuotaAmount':
                promedio.append(int(i[0]))            
        return 'Promedio: ' , round(sum(promedio)/len(promedio),2)
print(ReadFile())
"""

# 2da forma por comprension
"""
import csv
def ReadFile():
    with open('pregunta6.csv','r') as f :
        ejemplo = csv.reader(f)
        promedio=[int(i[0]) for i in ejemplo if i[0]!='QuotaAmount']
        return 'Promedio-> ' , round(sum(promedio)/len(promedio),2)
print(ReadFile())
"""
"""
PREGUNTA 7
Del ejercicio anterior cree dos pruebas unitarias (use unittest), una que 
compare el valor de retorno con "146633.33" y el otro con "15000" [150000], ambos test deben dar "Ok" como salida.

Recuerde usar la palabra "test" al inicio de cada función con su prueba.

"""
"""
import unittest
import csv

# Definimos las funciones para usar unittest
def averageCsv():
    with open("pregunta6.csv") as f:
        read = csv.reader(f)
        datos = [int(i[0]) for i in read if i[0].isnumeric()]
        average = sum(datos)/len(datos)
        print(average)
    return average

averageCsv()

def first_term():
    with open("pregunta6.csv") as f:
        read = csv.reader(f)
        datos = [int(i[0]) for i in read if i[0].isnumeric()]
        first_term = datos[0]
        print(datos[0])
    return first_term

first_term()


# UNIT TEST - promedio

class csv_correctly(unittest.TestCase):
    
    def test_average(self):
        average1 = 146633.33333333334
        average = averageCsv()
        self.assertEqual(average, average1)
    
if __name__=="__main__":
    unittest.main()


# UNIT TEST - primer termino

class csv_correctly(unittest.TestCase):
    
    def test_firstterm(self):
        first_term1 = 150000
        first_term  = first_term()
        self.assertEqual(first_term1, first_term)
    
if __name__=="__main__":
    unittest.main()
"""
# Funcion promedio 
# Primer valor de la tabla

# csv_correctly si el primer valor es 150000 es leido correctamente, sino esta equivocado.

"""
import unittest
class prueba(unittest.TestCase):
    def test(self):
        self.assertTrue("15000")

if _name_ == "_main_":
    unittest.main()

class prueba(unittest.TestCase):
    def test(self):
        self.assertTrue("146633.33")

if _name_ == "_main_":
    unittest.main()
"""
"""
PREGUNTA 8
Obtenemos prácticas en una laboratorio de una universidad y nos solicitan 
implementar de un paper la siguiente expresión matemática:


Siendo:

e la constante de Euler
log es logaritmo
cos es el coseno

"""
"""
import math

num_begin = 1
num_last  = 9
result = []

for i in range(num_begin, num_last+1):
    result.append(math.cos(math.log(math.e*i)))
    
print(sum(result))
"""
"""
# 2da forma:
import math

num_begin = 1
num_last  = 9

result = [math.cos(math.log((math.e)*i)) for i in range(num_begin, num_last+1)]
print(sum(result))
"""

"""
import math
print(math.cos(math.log((math.e)*4)))
"""

"""
PREGUNTA 9
Recolectar los feriados del 2022.

Al ingresar una fecha inicial y días hábiles Generar un código 
que permita encontrar la fecha siguiente sin considerar fines de semana (sábado y domingo) ni feriados.

"""
# Si el dia que le ingresamos es sabado o viernes, entregar el lunes
# Si el dia siguiente es un feriado, hasta que un dia sea un dia habil. [puentes] 
# While o recursividad. Lo idoneo es while.
