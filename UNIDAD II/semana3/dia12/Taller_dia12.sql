-- Usando la base de datos world
-- Ejemplos de la clase MySQL del dia 03/11/2022

Use world;

# Select en country con limite "Limit 1,15" el 1: indica el Offset o fila en la que empieza a contar
# y 15: Indica el número de registros
Select *
From country
Limit 1,15;

# Para consultar valores unicos, usamos "Distinct" luego de Select
Select Distinct continent
From country

# Seleccionamos varias columnas
Select Name, continent
From country

/*
ORDENAMIENTO DE LOS DATOS - Order by
*/

# Menor a mayor por defecto
# Asc acendente
# Des descendente
-- Ordenamiento Descendente
Select *
From country
Order by Population Desc, GNP;

-- Ordenamiento Ascendente
Select *
From country
Order by Population Asc, GNP;

/*
Ordenamiento ppor indexes: Simulando llamar a las variables
Para el caso del ejemplo es 1-name y 2 population 
Los numeros deben ser la misma cantidad de columnas seleccionadas
*/

Select Name, Population
From country
Order by 1, 2;

/*
Usamos los varlores negativos con el indexes [averiguar sobre los valores negativos]
*/
Select Name, Population, GNP
from country
Order by 1, 2, 3

/*
FILTROS - En ingles: Filters
*/

/*
Condicionales para el caso MySQL
= : igual
!= or <> : diferente
Between, And : rango
Is Null   : No value, no es igual a vacio o cero, columnas con valores nulos
Is Not Null: valores que no sean nulos
*/

# "Where" nonmatches
Select *
From country
Where Continent <> "Africa"

Select *
From country
Where Continent != 'Asia'

# 'Where' con rango de valores // Between - And
Select *
From country
Where Population Between 1000000 and 2000000

# 'Where' con no value Null, es diferente a 0, string vacio "" o espacios
Select *
From country
Where GNPOld Is Null;

Select *
From country 
Where GNPOld Is not Null And IndepYear Is Not Null;
# Where GNPOld and IndepYear Is Not Null [Pero también habria un problema con el is]

/*
FILTROS AVANZADOS
*/

# Combinando 'Where' con el operador "And"
Select * 
From country
Where IndepYear > 1500 And Continent = 'South America';

# Combinando 'Where' con el operador "Or"
Select *
From country
Where IndepYear > 1500 Or Continent = 'South America'

# Combinando 'Where' con operadores

# Combinando "Where" con operadores, se pueden usar parentesis
/*
Ejemplo: Mostrar todos los paises donde el IndepYear es mayor a 1000, 
y el continente sea Asia o Europa
*/
Select *
From country
Where IndepYear > 1000 And (Continent = 'Asia' Or Continent = 'Europe')

# Combinando "Where" con operador "in"
Select *
From country
Where IndepYear > 1000 and Continent in ('Asia', 'Europe')

# Combinando "Where" con operador "Not in"
Select *
From country
Where IndepYear > 1000 and Continent Not in ('Asia', 'Europe')

/*
Otros Ejemplos
*/

Select *
From country 
Where Continent In ("Asia", "Europe")

Select *
From country 
Where Continent Not in ("Asia", "Europe")

/*
OPERADOR LIKE - like, busqueda de patrones // En bibliografia se le encuentra en Wildcard filtering
*/

# Que comience con "Ba"
Select * 
From country
Where Name like 'ba%'

# QUe termine con "Ba"
Select * 
From country
Where Name like '%Ba'

# Contenga "Ba", no interesa donde
Select * 
From country
Where Name like '%Ba%'

/*
CREAMOS UNA TABLA
*/

use world
Create Table hola (
	'nombre' VarChar(45),
    'numero' Int
); 

Insert Into hola
(nombre, numero)
Values
('Marcos', 12)

# No se consideran los elementos nulos
Select *
From hola
Where nombre Like %


/*
EJERCICIO DE CLASE
*/
Use world

Select *
From city
Where CountryCode like "_D_"

# Segunda letra en "n" de los nombres
Select *
From country
Where Name Like '_n%'

# Todos los nombres que empiecen con la 'o' y termine con la 'a'
Select *
From city
Where Name Like 'O%a' 

/*
EJERCICIO PROPUESTOS
*/

# Ciudades donde contenga una 'o' y luego 'a'
Select *
From city
Where Name Like '%o%a%'

# Mostrar todas las ciudades donde el nombre contenga una a, el country code empiece en A o finalice en W, o la poblacion sea mayor a 5000000
Select *
From city
Where Name Like '%A%' And (CountryCode Like 'A%' or CountryCode Like '%W') Or Population > 5000000

/*
Mostrar todos los paises que no tengan valores 
nulos en ninguna de sus columnas, ordenarlo 
mediante su GNP. Ademas, considerar que deben 
ser de los siguientes continentes: North America, 
Asia o Europe y verificar que su GNPOld sea menor 
al GNP actual.
*/
Select *
From country
Where Name Like "%" Order By GNP and (Continent in ('North America', 'Asia' , 'Europe') And GNPOld < GNP)

Select *
From country
Where (IndepYear Is Not Null And LifeExpectancy Is Not Null And GNPOld Is Not Null) 
And Continent In ('North America', 'Asia' , 'Europe')
And GNPOld < GNP
Order by GNP Desc
Limit 10




