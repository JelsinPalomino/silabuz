Use world;

Select *
From country;

/*
EJERCICIO 1: Mostrar el promedio por continente del GNP
*/

Select Continent, avg(GNP) as "Promedio GNP"
From country
Group by Continent
;

/*
EJERCICIO 2: Mostrar el promedio por region de LifeExpectancy solo 
de aquellos que fuesen una forma de republica.
*/
# avg si encuentra valor nulo lo va anular el resultado 
Select Region, avg(LifeExpectancy)
From country
Where GovernmentForm like "%Republic%"
And LifeExpectancy Is not Null
Group by Region;

/*
EJERCICIO 3: Mostrar por regiones, los promedios de todas 
las columnas que se puedan calcular, ademas mostrar el 
anio minimo de independencia y el maximo.
*/

Select * 
From country;

Select Region, 
avg(SurfaceArea) as AreaPromedio, 
avg(IndepYear) as AnioINdependenciaPromedio, 
min(IndepYear) as AnioIndependenciaMinimo, 
max(IndepYear) as AnioIndependenciaMaximo, 
avg(Population) as PoblacionPromedio, 
avg(LifeExpectancy) as VidaPromedio, 
avg(GNP) as GanaciaPromedio, 
avg(GNPOld) as GananciaPromedioAntiguo
From country
Where IndepYear Is not Null
And LifeExpectancy Is not Null
And GNPOld Is Not Null
Group by Region;











