Use world;

# UPDATE - command
# Ejercicio 1
Select * 
From alumnos_nuevos;

Update alumnos_nuevos
Set
	nombre_nuevo = "Anthony"
Where nombre_nuevo = "Anthony"


# Ejercicio 2
Select *
From alumnos;

Update alumnos
Set
	apellidos = Null
Where apellidos = "Dia"

# "UPDATE IGNORE" // NO es recomendable usar, porque si sale un error es mejor 
# verificar el error

# DELETE // 
Select * 
From alumnos_nuevos;

# Con esto se borra toda la información
Delete From alumnos_nuevos;

# Para especificar que borrar, se usa el comando WHERE
Delete From alumnos_nuevos
Where apellidos_nuevo = "Dia"

# CAMPOS CALCULADOS // son las columnas creadas con alteraciones creadas con la información
# actual
# AS : alias

Select nombre as NombresDelAlumnos
From alumnos;

# CONCATENAR COLUMNAS // CONCAT . funcion de sql
# Ambos campos deben tener valores, porque sino resulta NULO 
Select concat(nombre, " ", apellidos) 
From alumnos

Select concat(nombre, " ", apellidos) as "Nombres y apellidos"
From alumnos;

# Limpiar espacios de texto
Select * 
From alumnos_nuevos;

Insert into alumnos_nuevos
()
Values
("   Pablo", "   Marmol"),
("Leonard   ", "Hobstater   "),
("   John   ", "   Snow   ")

# Limpieza de espacios con "RTrim"
# rtrim para la derecha, desde la ultima letra
# ltrim para la izquierda
Select ltrim(rtrim(nombre_nuevo)) as Nombres, ltrim(rtrim(apellidos_nuevo))
From alumnos_nuevos;

# Concatenamos los valores de las columnas
Select concat(ltrim(rtrim(nombre_nuevo)), " ", ltrim(rtrim(apellidos_nuevo))) as NombresCompletos
From alumnos_nuevos;

# OPERACIONES ENTRE COLUMNAS // todos tienen el mismo promedio, se usara where
Select nombre, apellidos, ((nota_1+nota_2+nota_3)/3) as PromedioDeNotas
From alumnos;

# FUNCIONES DE MANIPULACION DE DATOS
Create table textos(
	id Int,
    texto VarChar(150)
);

Insert into textos()
Values
	(1, "Este es un texto corto"),
    (2, "Este es un texto largo con muchas palabras que puedan o no tener sentido")

Select *
From textos;

# UPPER // command todo mayuscula
Select id, upper(texto)
From textos;

# LEFT(), LENGTH(), LOWER(), LOCATE(), SUBSTRING()
Select id, lower(texto)
From textos;

Select id, length(texto)
From textos;

Select id, substring(texto, 5, 30)
From textos;

Select id, locate('texto', texto)
From textos;

Select id, locate('un', texto)
From textos;

Select id, left(texto, 25)
From textos;

# MANIPULACION DE DATOS NUMERICOS
# retornar valor absoluto: ABS
Select *
From alumnos;

Insert into alumnos
()
Values
("Marcelo", "Coronel", 15,11,-18)

# usamos ABS
Select nombre, apellidos, abs(nota_3)
From alumnos;

# COS, EXP _ , MOD _ modulo, SQRT _ raiz cuadrada

Create Table alumnos(
	`nombre` VarChar(45),
    `apellidos` VarChar(45),
    `nota_1` Int,
    `nota_2` Int, 
    `nota_3` Int
);

Insert into alumnos
()
Values
("Mario", "Santivañez", 15, 11, 18),
("Carlos", "Mendoza", 12, 10, 12),
("Maria", "Solis", 13, 5, 15),
("Isabel", "Reyes", 14, 9, 20)

Select mod(nota_1, 2)
From alumnos;

Select sqrt(nota_1)
From alumnos;

# MANIPULACION DE FECHAS EN TABLAS SQL

Use sakila;
Select * 
From film

# DAYOFWEEK()
Select dayofweek(last_update)
From film;

# ADDDATE, ADDTIME, CURRDATE, CURRTIME, 
Select curdate()
From film
Limit 1;

Select curtime()
From film
Limit 1;

Select datediff(curdate(), last_update)
From film
Limit 1;

Select day(last_update)
From film
Limit 1;

Select month(last_update)
From film
Limit 1;

Select monthname(last_update)
From film
Limit 1;

Select last_update
From film
Limit 1;

Select adddate(last_update, Interval 3 day)  #month, year, quarter [trimestre]
From film
Limit 1;

Select date_add(last_update, Interval 3 day)  #month, year, quarter [trimestre]
From film
Limit 1;

# FUNCIONES DE AGREGACION DE DATOS
# GROUP BY

Use world;

Select * 
From country;

# Agrupamos por continente
Select * 
From country
Group by Continent;

Select nombre, nota_1, nota_2, nota_3 
From alumnos
Group by apellidos;

Select *
From country
Group by Region;

# USAMOS TAMBIÉN LA CLAUSULA HAVING
# Funciona como un WHERE al momento de agrupar 
# Son los que encontro primero
# lo ideal es un where, no se usa mucho having
Select *
From country
Group by Continent
Having GovernmentForm = "Republic";

# Otro ejemplo en este caso solo un resultado
Select avg(nota_1) 
From alumnos;

Select nombre, avg(nota_1) 
From alumnos;

Select nombre, avg(nota_2) 
From alumnos;

Select nombre, avg(nota_3) 
From alumnos;

# COUNT
Select count(nombre)  # una columna en especifico
From alumnos;

Select count(*)    # * para todo
From alumnos;

Select max(nota_1) as Nota1Maxima, max(nota_2) as Nota2Maxima, max(nota_3) as Nota3Maxima   
From alumnos;

# Nullos

Select count(Name)
From country;

# Salta aquellos registros con valores nulos
Select count(IndepYear)
From country;

# SUM // en la suma un dato negativo lo restara
Select sum(nota_1) as SumaNota1 
From alumnos;

# DISTINCT Y COUNT
Select count(distinct Continent)
From country;




