-- CLASES DIA 14
-- PARTE 1: ejercicios sobre subconsultas, inner y otros
--

Use world;
Create table alumnos(
	`nombres` VarChar(45),
    `apellidos` VarChar(45),
    `notas` Int
);

Insert into alumnos()
Values 
("Pedro", "Ramirez", 12),
("Juan", "Perez", 14),
("Carlos", "Santos", 17),
("Isabel", "Diaz", 16),
("Marcelo", "Samaniego", 11);

# Ejemplo 1
Select * 
From alumnos
Where notas > (
	Select avg(notas)
    From alumnos
	);

#

# EJEMPLO INNER
Use world;

Create table alumnos(
	`id` Int,
	`nombres` VarChar(45),
    `apellidos` VarChar(45),
    `idSalon` Int
    );

Create table salones(
	`id` Int, 
    `aula` VarChar(20),
    `horaEntrada` Time
	);

Insert into alumnos()
Values 
(1, "Pedro", "Ramirez", 1),
(2, "Juan", "Perez", 2),
(3, "Carlos", "Santos", 3),
(4, "Isabel", "Diaz", 3),
(5, "Marcelo", "Samaniego", 2),
(6, "Maria", "Salazar", 3);

Insert into salones()
Values 
(1, "Aula A", "08:00:00"),
(2, "Aula B", "12:00:00"),
(3, "Aula C", "16:00:00");


# Ejemplo1 de INNER_JOIN
Select al.nombres, al.apellidos, sal.aula, sal.horaEntrada
From alumnos as al 
Join salones as sal
On al.idSalon = sal.id

# Ejemplo2 de SEFL_JOIN

Create table empresas(
	`id` Int,
    `nombre` VarChar(45),
    `idProv` Int
);

Insert into empresas ()
Values
(100, "Empresa A", -1),
(210, "Empresa B", 301),
(301, "Empresa C", 100),
(400, "Empresa D", 100),
(520, "Empresa E", 100),
(36500, "Empresa F", 301);

-- Vemos el ejercicio
Select A.nombre as Empresa, B.nombre as Proveedor
From empresas A Join empresas B
On A.idProv = B.id;

/*
Ejemplo3 de LEFT_JOIN
*/
Create table proveedor(
	`id` Int,
    `nombre` VarChar(45)
);

Create table comprador(
	`nombre` VarChar(45),
    `idprov` Int
);

Insert into proveedor()
Values
(203, "Prov 1"),
(204, "Prov 2"),
(205, "Prov 3");

Insert into comprador()
Values
("Comprador 1", 203),
("Comprador 2", 204),
("Comprador 3", 204),
("Comprador 4", 0);

# exmple lef join
Select * 
From proveedor p Left Join comprador as c
On p.id = c.idprov;

# ejenplo rgigth join
Select * 
From proveedor p Right Join comprador as c
On p.id = c.idprov;

# 
Select * 
From proveedor p Left Join comprador as c
On p.id = c.idprov
Union
Select * 
From proveedor p Right Join comprador as c
On p.id = c.idprov;

/*
Resumen:
- Self join: Para referenciar datos de una misma tabla
- Right Join: Para obtener datos de una tabla externa
- Left Join: Para obtener datos de una tabla externa
- Full Join: 
- Inner Join: Para obtener los datos que coinciden en dos tablas / cuando solo se quiere información de 
ambas tablas. Nos importan los datos que tengan valores 
- Cross Join:

*/

/*
CONSULTAS COMBINADAS
- UNION para consultas complejas
*/

/*
Si queremos obtener las empresas con un id mayor a 350 y 
proveedor con id mayor a 200. Ademas, empresas con id menor 
a 250 y proveedor con id distinto de 100
*/ 

Select *
From empresas
Where (id > 350 and idprov > 200)
Or (id<250 and idprov != 100);

# Normalmente se hacen uso de UNION para consultas mas complejas
Select *
From empresas
Where id > 350 and idprov > 200
Union
Select *
From empresas
Where id<250 and idprov != 100;

Select *
From empresas
Where id > 350 and idprov > 200
Union
Select *
From empresas
Where id<250 and idprov != 100
Order by nombre;

-- PARTE 2: Expresiones regulares
-- Regular expression (regex)
# Patron de busqueda para encontrar patrones dentro de cadenas
# Similar a LIKE

Create table regexej(
	`id` Int, 
    `palabra` VarChar(100)
);

Insert into regexej()
Values
(1, "1301 Rad"),
(2, "2430 Mad"),
(3, "1001 Vad"),
(4, "3140 Marad"),
(5, "4101 Rad");

# ejemplos
Select *
From regexej
Where palabra regexp "30";

# ejemplos
Select *
From regexej
Where palabra regexp "30|rad";

Select *
From regexej
Where palabra like "%30%" Or palabra Like "%rad%";

# BUscar caracteres especificados
Select *
From regexej
Where palabra regexp "[135] rad";

Select *
From regexej
Where (palabra like "rad%" And palabra Like "%1%")
or (palabra like "rad%" And palabra Like "%1%")
or (palabra like "rad%" And palabra Like "%1%")
;

# Caracteres opcionales
# LIKE: encuentra string completas
# REGEX: qUE 


-- PARTE 2: Full Text Searching
-- 

Create table textos(
	`id` int,
    `texto` VarChar(50)
);

Alter table textos
Add fulltext(texto);

Insert into textos ()
Values 
(1, "Este es SQL"),
(2, "Este es SML"),
(3, "Este es SVL"),
(4, "SQL"),
(5, "SQL SQL SQL");

# Ejmplo. el Indexado se da en ADD FULLTEXT
Select texto
From textos
Where Match(texto) Against ('SQL');


Select nombres
From alumnos
Where Match(nombres) Against ('o');

Select texto, Match(texto) Against ('SQL') as coincidencia
From textos;

# para textos de InnoDB o MyISAM
/*
Full text solo se puede usar con  VarChar, Char, Ttexti
1.- Natural languaje mode
2.- Boolean mode
	Palbras a emparejas, a exluir y expressión groppin  Mysql
3.- Query expaksion mode
    
*/

Select texto, 
From textos
Where Match(texto) Against ('SQL' with query expansion);











