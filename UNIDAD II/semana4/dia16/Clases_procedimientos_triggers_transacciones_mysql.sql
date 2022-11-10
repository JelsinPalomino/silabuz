-- DIA 16

-- PARTE : CREACION DE PROCEDIMIENTOS
# --------------------------------------

# CREAMOS LA DATABASE ejemplo y lo usamos
create database ejemplo;
Use ejemplo;

Create table aulas(
	id int Primary Key,
    nombre Varchar(100)
);

create table alumnos(
	id int Primary Key auto_increment,
    nombre varchar(100),
    apellido varchar(100),
    idAula int,
    Foreign key (idAula) references aulas(id)
);

Insert into aulas()
Values
(20, "Aula A"),
(21, "Aula B"),
(22, "Aula C"),
(23, "Aula D");

Insert into alumnos(nombre, apellido, idAula)
Values
("Marcelo", "Salas", 20),
("Maria", "Lopez", 21),
("Isabel", "Rodriguez", 22),
("Carlos", "Chavez", 23),
("Santiago", "Perez", 21),
("Luz", "Solano", 22),
("Juana", "Casas", 23),
("Isaac", "Samaniego", 20);

# CREAMOS EL PROCEDIMIENTO ALMACENADO

-- Creamos el procedimiento almacenado
-- Ejemplo1
use ejemplo;

Delimiter //
Create procedure salones()
begin
	select A.idAula, Count(*) as "Número de alumnos"
    from alumnos A
    group by A.idAula;
End; //
Delimiter ;

-- Llamamos al procedimiento almacenado
Call salones();


-- Ejemplo2:
-- creamos el procedimiento: VARIABLES DE SALIDA
Use ejemplo;
Delimiter //
Create procedure minmaxSalones(out minInicial int, out maxInicial int)
Begin
	Select min(a.idAula) 
    into minInicial
	from alumnos a;
    Select max(a.idAula)
    into maxInicial
	from alumnos a;
End; //
Delimiter ;

-- 1ros resultados
-- llamamos al procedimiento
Call minmaxSalones(@minInicial, @maxInicial);
-- llamamos los resultados
Select @minInicial, @maxInicial;              # van a existir porque son variables de la BD

-- 2do resultados
-- usamos otro nombre para los resultados del procedimiento
Call minmaxSalones(@minInicialSalon, @maxInicialSalon);
Select @minInicialSalon, @maxInicialSalon;

-- Ejemplo3
-- Creamos el procedimiento: VARIABLES DE ENTRADA
-- prueba: primera forma
Delimiter //
Create procedure contarSalonesDiferentes(In idR int, Out countId int)
Begin 
	Select count(a.id)
    From aulas a
    Where idR <> a.id
    Into countId;
End; //
Delimiter ;

Call contarSalonesDiferentes(20, @conteo);
Select @conteo;

-- prueba de segunda forma
-- No habra problema porque asigna "Into" todo el resultado,
-- no hay diferencia de donde se le ponga
-- Pero se debe tener cuidado de los campos que se este seleccionando
-- Si hay varios parametros de salida, se debe tener cuidado

Delimiter //
Create procedure contarSalonesDiferentes(In idR int, Out countId int)
Begin 
	Select count(a.id)
    From aulas a
    Where idR <> a.id
    Into countId;
End; //
Delimiter ;

Call contarSalonesDiferentes(20, @conteo);
Select @conteo;


-- Ejemplo4
-- Creamos procedimiento: DROP PROCEDURE

Delimiter //
Create procedure contar123qwe(In idR int, Out countId int)
Begin
	Select count(a.id)     
    From aulas a
    Where idR <> a.id
    Into countId;
End; //
Delimiter ;

Drop procedure contar123qwe;

-- Ejemplo 5:
-- Estas variables que se generan son de sesion.

use ejemplo;

Call minmaxSalones(@var1, @var2);
Select @var1, @var2;

/*
EJEMPLOS DE LA CLASE
*/

# Listar los 7 proveedores de productos a partir del registro numero 5
Select * 
From products;

Delimiter //
Create procedure seven_prov()
begin
	Select productVendor as Proveedores
    From products P
    Limit 4, 7;
end; //
Delimiter;
call seven_prov;

# Listar los proveedores de productos que contengan la palabra Classics
Delimiter //
Create procedure word_classics()
begin
	Select productVendor as ProveedoresConClassics
    From products P
    Where productVendor regexp "Classics"
    group by productVendor;
end; //
Delimiter ;
Call word_classics;

drop procedure word_classics;

# CASO SOBRE VARIACION 
# 1ra pregunta
Use classicmodels;

Delimiter //
Create procedure listarProveedores(In offsetRes int, In cantReg int)
Begin
	Select productVendor
    From products
    Group by productVendor
    Limit offsetRes, cantReg;
End; // 
Delimiter ;

Call listarProveedores(4, 7);
Call listarProveedores(6, 2);
Call listarProveedores(11, 6);
Call listarProveedores(13, 5);
Call listarProveedores(2, 3);

drop procedure listarProveedores;

# 2da pregunta
Delimiter //
Create procedure proveedorPalabra(In palabra VarChar(30))
Begin
	Select productVendor
    From products
    Where productVendor Like concat("%",palabra,"%")
    Group by productVendor;
End; //
Delimiter ;

Call proveedorPalabra("Classics");
Call proveedorPalabra("Metal");
Call proveedorPalabra("Motor");
Call proveedorPalabra("Mini");
Call proveedorPalabra("art");

-- PARTE : USO DE LOS CURSORES
# --------------------------------------
Use ejemplo;

Delimiter //
# 1.- Declaramos el cursor
Create procedure cursorEjemplo()
Begin
	Declare idAlum cursor
    For
    Select a.id From alumnos a;
    
    open idAlum; 
    
	fetch 
    next
    
    close idAlum;
End; //
Delimiter ;


-- PARTE : USO DE TRIGGERS
# --------------------------------------
Use ejemplo;

# CREATE TABLE
Create table test1(a1 int);
Create table test2(a2 int);
Create table test3(
	a3 int not null auto_increment Primary key
);
Create table test4(
	a4 int not null auto_increment Primary key,
    b4 int default 0
);

# INSERT - VALORES
Use ejemplo;

Insert into test3(a3)
values
(null),
(null),
(null),
(null),
(null),
(null),
(null),
(null),
(null),
(null);

Select *
From test3;


Insert into test4(a4)
values
(0),
(0),
(0),
(0),
(0),
(0),
(0),
(0),
(0),
(0);

Select *
From test4;

# PARTE: USO DE LOS TRIGGER
Delimiter |
Create trigger testref Before insert on test1
	for each row
    begin 
		insert into test2 set a2 = New.a1;
        Delete from test3 where a3 = New.a1;
        Update test4 Set b4 = b4 + 1 Where a4 = New.a1;
    end; |
Delimiter ; 

Insert into test1()
Values
(1),
(3),
(1),
(7),
(1),
(8),
(4),
(4);

Select * From test1;
Select * From test2;
Select * From test3;
Select * From test5;















