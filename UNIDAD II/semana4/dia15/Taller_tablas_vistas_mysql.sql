-- DIA 14: CREACION DE TABLAS Y VISTAS

/*
EJERCICIO1: 
- Plataforma: Datos Abiertos de Perú.
- Tópico: Datos de afiliados al SIS en estado activo.
- Link de plataforma: Link Datos Abiertos.

Datos adaptados para csv: Link Silabuz.
Del CSV indicado, necesitamos que se cree una tabla acorde a los 
atributos de las columnas. Se parte de que la data se encuentra 
como strings y se necesitan realizar algunas alternaciones:

- Fecha de corte DATE
- Ubigeo INT
- COD_UNIDAD_EJECUTORA INT
- CODIGO_IPRESS INT
- EDAD INT
- TOTAL_AFILIADOS INT

En los campos restantes, cuentan como máximo con 100 caracteres.
Recuerde importar los datos tal y como están, y luego realice las 
alteraciones en los campos de la tabla.
Para la carga de datos utilice el comando LOAD
*/

create database SIS;
use sis;

create table unidad_ejecutora(
	idUniEje int primary key not null, 
    nombre varchar(100)
);

create table ipress(
	idIpress int primary key not null,
    nombre varchar (100)
);

# un campo calculado no se pone como atributo, en terminos de diseño
# no se le debe incluir. 
create table afiliados_salud(
	documento_identidad int primary key not null,
    fecha_corte date,
    ubigeo int,
    COD_UNIDAD_EJECUTORA int,
    CODIGO_IPRESS int,
    EDAD int,
    TOTAL_AFILIADOS int,
    foreign key (COD_UNIDAD_EJECUTORA) references unidad_ejecutora(idUniEje),
    foreign key (CODIGO_IPRESS) references ipress(idIpress)
    
);

alter table afiliados_salud modify column ubigeo int default "000000";
alter table afiliados_salud add column sintomas varchar(200) default "Sin sintoma";
alter table afiliados_salud drop column TOTAL_AFILIADOS;

create table ubigeo(
	idUbigeo int primary key not null,
    region varchar(50),
    provincia varchar(50),
    distrito varchar(50)
);

alter table afiliados_salud add constraint fk_ubigeo 
foreign key (ubigeo) references ubigeo(idUbigeo);

/*
EJERCICIO 2:
Plataforma: Datos Abiertos de Perú.
Tópico: Licenciamiento Institucional de las Universidades peruanas.
Link de plataforma: Link Datos Abiertos.
Datos adaptados para csv: Link Silabuz.
A partir del archivo csv crear una tabla, tomando en cuenta lo siguiente:

Campo	                Consideración
NOMBRE	                500 caracteres
TIPO_GESTION	        400 caracteres
ESTADO_LICENCIAMIENTO	400 caracteres
UBIGEO	                  8 caracteres

Los demás campos de texto cuenta con un tamaño de 200 caracteres. 
Asimismo realizar la conversión adecuada de los campos Latitud y Longitud.
Finalmente contabilizar los diversos tipos de Estado de Licenciamiento 
de la Entidad de Estudios: ESTADO_LICENCIAMIENTO.

*/

-- TEMA: VISTAS USAMOS LA DB CLASSICMODELS
/*
EJERCICIO1: 
Crea una vista que tenga los siguientes atributos:

Nombre del producto
Cantidad total del producto ordenado
Número total de ordenes
*/
-- Siempre hacerlo con la llave primaria | el peligro es tener datos repetidos
-- luego hacerlo 

# Luego, con la vista creada obtenga el nombre producto con el número máximo de productos ordenados
CREATE VIEW totalProductos AS 
SELECT 
  P.`productName` AS `Nombre del producto`, 
  SUM(OD.`quantityOrdered`) AS `Cantidad total ordenada`, 
  COUNT(*) AS `Número de pedidos` 
FROM 
  products P 
  JOIN orderdetails OD ON P.`productCode` = OD.`productCode` 
GROUP BY 
  P.`productName`;
  
# Obtenemos el producto con la cantidad máxima de productos ordenados
SELECT 
  T.`Nombre del producto` 
FROM 
  totalProductos T 
WHERE 
  T.`Cantidad total ordenada` = (
    SELECT 
      MAX(T.`Cantidad total ordenada`) 
    FROM 
      totalProductos T
  );


/*
EJEMPLO_TALLER:
Listar los productos que fueron vendidos a clientes de Paris, 
cuyo monto supera los 1000 [order]
*/
create view productClientParis as
	select C.customerNumber, sum(P.amount) as total
	from customers C inner join payments P
	On C.customerNumber = P.customerNumber
    Where C.city = "Paris"
	Group by C.customerNumber having total > 1000;

select * 
from products p inner join orderdetails od 
on p.productCode = od.productCode
inner join orders o
on o.orderNumber = od.orderNumber
inner join customers c
on c.customerNumber = o.customerNumber
where customerName in (select customerName from productClientParis)






