-- DIA15: CLASE | CREACION DE TABLAS Y VISTAS 
-- Llaves primarias y llave foranea
--
# Llave primaria es de la primera tabla,
# cuando se usa en otra tabla, se llama llave foranea 
# puede estar conformada por uno o mas atributos

# Ejemplo1 de primary key
Use world;

Create table ejemplo1(
	num int Primary Key
);

Insert Into ejemplo1()
Values
(1),
(2),
(3),
(4),
(5);

Select * 
from ejemplo1;

# Ejemplo de primary key multiple
-- No son algo comun, pero si se usan
-- El * tambien puede significar, primary key y también obligatorio

Create table ejemplo2(
	id Int, 
    nombre VarChar(200),
    Primary key (id, nombre)
);

Insert into ejemplo2()
values
(101, "Marcelo"),
(102, "Juan"),
(103, "Pedro"); 

Select * 
From ejemplo2;

Insert into ejemplo2()
Values
(101, "Bartolomeo");

Insert into ejemplo2()
Values
(104, "Juan");

# Reciben porque son llaves compuestas, y son diferentes. 
-- Usamos cuando se requiere llaves compuestas, al principio de la creacion de las bases de datos
-- Para crear codigos de productos y otros de esa naturaleza. Para tablas intermedias

Select * 
From ejemplo2
Where id = 101 and nombre = "Marcelo";

# EJEMPLO3
Create table ejemplo3(
	idExam Int Primary Key,
    curso VarChar(100),
    idAlumno Int,
    Foreign key (idAlumno) references ejemplo2(id)
);

Insert into ejemplo3()
Values
(400,"Matematica", 101),
(401,"Matematica", 102),
(402,"Matematica", 103);

select *
From ejemplo3;

Insert into ejemplo3()
Values
(404, "Matematica", 103);

# EJEMPLO9: solo por cuestion de consulta
Create table ejemplo3(
	idExam Int Primary Key,
    curso VarChar(100),
    idAlumno Int,
    nombre0 VarChar(200),
    Foreign key (idAlumno, nombre0) references ejemplo2(id, nombre)
);

-- TEMA: VALORES NULOS
-- Cuando podemos permitir los valores nulos, en el caso que tenemos un BD en desarrollo
# usamos el NOT NULL
Create table ejemplo4(
	id Int Primary Key,
	nombre VarChar(200) Not null
);

Insert into ejemplo4()
Values
(1, "MarcoS"),
(2, "Juan"),
(3, "Santiago"),
(4, "Maria"),
(5, "Isabel");

Select *
From ejemplo4;

Insert into ejemplo4()
Values
(6, Null);


# AUTO-INCREMENTO es de uno en uno
Create table ejemplo5(
	id Int primary key auto_increment,
    nombre VarChar(200) Not null
);

Insert into ejemplo5(nombre)
Values
("Marcelo"),
("Pedro"),
("Isaac"),
("Jeremy");

Select * 
From ejemplo5;

Insert into ejemplo5()
values
(101, "Marcelo")
;

Insert into ejemplo5(nombre)
values
("Ignacio");


# Usamos DEFAUT | valores por defecto
-- no admite nulos, pero que los datos a ingresar no todos cumplen esta 
-- condicion

Create table ejemplo6(
	id Int primary key auto_increment,
    nombre VarChar(200) Not null Default "Sin nombre"
);

Insert into ejemplo6()
Values
(),
(),
(),
(),
(),
();

Select * 
From ejemplo6;

# Como podemos insertar el nombre "Maria"
Insert into ejemplo6(nombre)
Values
("Maria");

-- Si no se ejecuta una sentencia, debemos volver a intentarlo un par de veces
-- al menos, para asegurarnos.

# TEMA: MOTORES DE ALMACENAMIENTO
-- Modulos de software que permiten escribir, leer y actualizar data en la base de datos
-- Se puede cambiar de acuerdo al tipo de traajo que necesitemos

show engines;

Create table ejemplo10(
	id int
) Engine = Archive;

Select *
From ejemplo10;

Show engines;

-- ARIA, no permite transacciones, y también añade seguridad

# TEMA: ACTUALIZACION DE TABLAS
-- Create | para crear
-- ALTER TABLE | para alterar tabla
/*
ADD COLUMN
DROP COLUMN
MODIFY COLUMN
ADD CONSTRAINT: restriccion, conocido como regla
*/

Alter table ejemplo6
Add column apellido VarChar(200) Not null Default "Sin apellido";  
#Not null:  Ingresa un empty string, sin nada adentro

Alter table ejemplo6
Drop column apellido;

# queremos que el nombre tenga un varchar 100
Alter table ejemplo6
Modify column nombre VarChar(100);
-- para modificar o arreglar que nos equivocamos un tipo de datos

Select * 
From ejemplo6;

# TEMA : LLAVES FORÁNEOS

-- Para el ejercicio creamos la tabla ejemplo7
Create table ejemplo7(
    nombre7 Varchar(200) Primary key
);

Create table ejemplo8(
    nombre8 Varchar(200)
);

Alter table ejemplo8
Add constraint fk_ejemplo8 Foreign key (nombre8) references ejemplo7(nombre7);

Select * 
From ejemplo8;

Create table ejemplo9(
	nombre7 Varchar(200) primary key
);

Drop table ejemplo9;

Select * From ejemplo3;

-- No se podra borrar porque esta referenciada en otras tablas
Drop table ejemplo2;


# 1ro borrar referencias, y luego eliminar la tabla
drop table ejemplo8;
Drop table ejemplo7;

# Hay formas de forzar u

# TEMA: RENOMBRAR TABLAS
create table proveedores(
	nombre8 VarChar(200)
);

Rename table proveedores to proveedores;
# tener cuidado con los nombres. 

# TEMA: VISTAS O EN INGLES VIEWS
-- son tablas virtuales, no son tablas propiamente dichas y que estan dentro 
-- de la base de datos.
-- las vistas contienen querys 

/*
- Controlar el acceso a los usuarios a nuestra información
- hacer consultas de vistas
- pruebas sin afectar los datos reales
- Tenemos integridad de los datos.
*/

# EJEMPLO: PROMEDIO DE CALIFICACIONES DE UNA LISTA DE ALBUMES
-- artNombre: dentro de albumes es un foreign key
-- Nombre: en la tabla artistas es un primary key

Create table artistas (
	nombre VarChar(200) Primary Key,
    pais VarChar(100),
	retirado Tinyint
);

Create table albumes(
	nombre Varchar(200) Primary key,
    artNombre VarChar(200),
    anio Decimal,
    Foreign key (artNombre) references artistas(nombre)
);

Insert into artistas ()
values
("David Bowie", "G. D.", 1),
("Justin Bieber", "Canada", 0),
("Lady Gaga", "EE. UU.", 0),
("Leonardo Cohen", "Canada", 0);

Insert into albumes ()
Values
("ARTPOP", "Lady Gaga", 2013),
("Dear Heather", "Leonardo Cohen", 2004),
("Old Ideas", "Leonardo Cohen", 2012),
("Popular Problems", "Leonardo Cohen", 2014),
("You want it darker", "Leonardo Cohen", 2016);


Create table evaluaciones(
	nAlbum VarChar(200), 
    nArtista VarChar(200),
    fuente VarChar(200),
    evalNum Decimal,
    Foreign key (nAlbum) references albumes(nombre),
    Foreign key (nArtista) references artistas(nombre)
);

Insert into evaluaciones()
Values
("ARTPOP", "Lady Gaga", "Rolling Stone", 60),
("ARTPOP", "Lady Gaga", "The Guardian", 66),
("ARTPOP", "Lady Gaga", "Uncut", 66),
("Dear Heather", "Leonardo Cohen", "Rolling Stone", 70),
("Dear Heather", "Leonardo Cohen", "The Guardian", 60);

# CREAREMOS UNA VISTA
-- las vistas trabajan con consultas
-- nombre de la vista no debe ser igual que el nombre de las tavblas
-- las vistas son perpetuas, dar acceso a las vistas para que no hagan
-- cambios en las tablas referidas
-- por un tema de seguridad de los datos.
/*
Promedio de la calificacion del albumn de un artista 
*/
Create view albumeval as
	Select nAlbum, nArtista, floor(avg(evalNum)) as promedio, 
	count(evalNum) as numeval
	From evaluaciones
	Group by nAlbum, nArtista;

Select *
From albumeval
Where nArtista = "Lady Gaga";

# desde backend que busque otro dato
Select *
From albumeval
Where nArtista = "Lady Gaga";



Alter Table evaluaciones
Drop column evalNum;


# PROCEDIMIENTOS ALMACENADOS
/*
Para insertar valores
parametros desde el backend a la base de datos y con eso ya se hace la consulta
Es mala practica hacer un 
insert into tabla, desde el backend es una mala practica porque no se quiere 
revelar las tablas, para añadir proteccion y que sea reutilizable.
*/


















