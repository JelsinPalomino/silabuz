-- EJERCICIOS PROPUESTOS DEL TALLER
-- 1er grupo de ejercicios propuestos
Select *
from customers

/*
EJERCICIO: Listar a los contactos y sus direcciones, considerar concatenar el primer
nombre y el primer apellido en un solo campo
*/
Select concat(contactLastName, " ",contactFirstName) as contactos
from customers;
/*
EJERCICIO: De la consulta anterior observamos algunos espacios en blanco denominados
trailing spaces. Depurar dichos campos para que la concatenacion de la consulta anterior
sea mas pulcra
*/
Select concat(rtrim(contactLastName), " ", rtrim(contactFirstName)) as contactos
from customers;
/*
EJERCICIO: De la consulta anterior ahora nos solicitan que el nuevo campo (obtenido 
de la concatenacion) se exprese en mayusculas
*/
Select upper(concat(rtrim(contactLastName), " ", rtrim(contactFirstName))) as contactos
from customers;
/*
EJERCICIO: De la consulta anterior agregar otra columna que indique el numero de 
caracteres del campo addressline1 y ordenar los datos en base a esta nueva columna
de mayor a menor 
*/
Select upper(concat(rtrim(contactLastName), " ", rtrim(contactFirstName))) as contactos, length(addressLine1) as longitud
from customers
Order by longitud Desc;

-- EJERCICIOS PROPUESTOS DEL TALLER
-- 2do grupo de ejercicios propuestos

/*
1. Mostrar el precio medio de los vehiculos de cada proveedor.
2. MOstrar el precio minimo de los vehiculos de cada proveedor
3. MOstrar el precio maximo de los vehiculos de cada proveedor
4. Mostrar la distribución de precios(minimo, maximo, valor medio y acumulado) 
 de los vehiculos de cada proveedor
5. Mostrar la distribución del numero de estados en las ordenes (tabla orders)
6. Dicha distribución debe ser mostrada ordenadamente de mayor a menor
*/
Select *
From products

# 1ro
Select productName, round(avg(buyPrice), 2)
from products 
group by productName

# 2do
Select ProductName, round(min(buyPrice), 2)
From products
Group by productName

# 3ro
Select ProductName, round(max(buyPrice), 2)
From products
Group by productName

# 4to
Select ProductName, 
round(min(buyPrice), 2), 
round(max(buyPrice), 2), 
round(avg(buyPrice), 2), 
round(sum(buyPrice), 2)
From products
Group by productName

# 5to
Select *
From orders

Select status, count(status)
From orders
Group by status
Order by count(status) Desc;




