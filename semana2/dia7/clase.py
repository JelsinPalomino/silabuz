"""
el promedio de edad
numero de mujeres y hombres
numero de sobrevivientes y fallecidos

"""
"""
# 1ra forma
import csv

def readFile():
    with open("titanic.csv", "r") as fileTitanic:
        titanic = csv.reader(fileTitanic)
        ageList = [int(row[5]) for row in titanic if row[5].isnumeric()]
        ageList.reverse()
        ageList.pop()
    average = sum(ageList)/len(ageList)
    print(average)
    return average

readFile()
"""
"""
import csv

def readFile():
    male = []
    female = []
    with open("titanic.csv", "r") as fileTitanic:
        titanic = csv.reader(fileTitanic)
        ageList = [int(row[5]) for row in titanic if row[5].isnumeric()]
        ageList.reverse()
        ageList.pop()
    average = sum(ageList)/len(ageList)
    print(average)
    return average, male, female

readFile()
"""

"""
import csv

with open('titanic.csv') as f:
    archivo=csv.reader(f)
    datos=[]
    f=[]
    m=[]
    for i in archivo:
        if i[4]=='male':
            m.append(i)
        elif i[4]=='female':
            f.append(i)
    print(len(f),len(m))
"""

