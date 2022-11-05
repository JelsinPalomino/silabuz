-- DIA 13: CLASES SOBRE MYSQL 
-- 
-- 
# CREAMOS UNA TABLA
Use world;
Create Table alumnos(
	`nombre` VarChar(45),
    `apellidos` VarChar(45),
    `nota 1` Int,
    `nota 2` Int, 
    `nota 3` Int
);

# PROCESAMOS
Select * 
From alumnos;

# No siempre es necesario insertar las propiedades, también funcionaria sin las parentesis
# Un unico registro
Insert into alumnos
()
Values
("Pedro", "Marmol", 12, 14, 17)

# Multiples registros
Insert into alumnos
()
Values
("Mario", "Santivañez", 15, 11, 18),
("Carlos", "Mendoza", 15, 11, 18),
("Maria", "Solis", 15, 11, 18),
("Isabel", "Reyes", 15, 11, 18)

# Con datos incompletos // Indica error con insuficientes valores para las columnas
Insert into alumnos
()
Values
("Marcelo", 12, 14, 17)

# Con datos incompletos agregando un nulo
Insert into alumnos
()
Values
("Marcelo", Null, 12, 14, 17)

# Solo un par de propiedades, lo demas se completa con nulos
Insert into alumnos
(nombre, apellidos)
Values
("Ramon", "Valdez");

# Uso de "INSERT SELECT"

# 1ro creamos una nueva tabla 
Create Table alumnos_nuevos(
	`nombre_nuevo` VarChar(45),
    `apellidos_nuevo` VarChar(45)
);

# ingresamso datos a la tabla alumnos[_nuevos
Insert into alumnos_nuevos
()
Values
("Sheldno", "Cooper"),
("Juan", "DIa"),
("Anthony", "Quispe"),
("Juan", "quispe")

Select *
From alumnos_nuevos;

Insert into alumnos (nombre, apellidos)
Select nombre_nuevo, apellidos_nuevo
From alumnos_nuevos

# SENTENCIA UPDATE

Select *
From alumnos_nuevos;

# Actualizar datos
Update alumnos_nuevos 
Set 
	nombre_nuevo = "Anthony"
    