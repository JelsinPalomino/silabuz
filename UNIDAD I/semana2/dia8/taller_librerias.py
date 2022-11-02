"""
Contexto
En las actividades anteriores exploramos la data del titanic usando import csv

Data a utilizar: https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

Ahora utilizaremos import pandas, pandas es una biblioteca muy popular.

Recordemos configurar un entorno virtual primero y posteriormente instalar pandas.

Volveremos a calcular:

El promedio de edad.
La distribución del sexo (número de mujeres vs varones).
El número de sobrevivientes y fallecidos.
Asimismo realizar los siguientes plots:

La distribución de los sobrevivienes y los que fallecieron
La distribución de lugares de donde se embarcaron los pasajeros.
"""
 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv", encoding="utf-8")

#df1 = df.fillna(0)
#average = sum(df[5])/len(df1[5])

#print(df["Age"].mean())

# print(df["Survived"].value_counts())
print(df["Embarked"].value_counts()["S"])
print(df["Embarked"].value_counts()["C"])
print(df["Embarked"].value_counts()["Q"])

print(df["Survived"].value_counts())

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

#plt.hist(df["Embarked"].value_count())
#plt.show()

"""
a = (df.groupby("Survived").agg(frequency=("Survived", "count")))
print(a)


plot = df["Survived"].plot.bar(rot=0)
plot.show()

freq_by_species = (df 
  .groupby("Survived")
  .agg(frequency=("Survived", "count"))
  .reset_index())
  
(ggplot(freq_by_species, aes(x = "Survived", y = "frequency")) +
  geom_bar(stat = 'identity'))

freq_by_survived = (df.groupby("Survived").agg(frequency=("Survived", "count")).reset_index())
"""

