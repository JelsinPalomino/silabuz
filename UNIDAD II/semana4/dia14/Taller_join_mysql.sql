-- TALLER dia 13: SUBCONSULTAS, JOIN, CONSULTAS COMBINADAS
--

/*
PREGUNTA 1: Obtener el nombre de los clientes que viven en Francia y en
Paris
*/

select customerName
From customers
where city = "Paris" and country = "France";

/*
PREGUNTA2: De tabla payments filtrar aquellos registros cuyos montos sean superiores al promedio. 
A cada registro filtrado indicar los datos del cliente (customerNumber y customerName) 
y solo considerar a clientes de la ciudad de París.

-- En principio los join con menor cantidad de datos
-- Dentro de where donde hay selects, se podria poner campos a la derecha para optimizar.
-- la consulta.
*/

Select C.customerNumber, C.customerName
From (select *
From customers Where country = "France") C inner join payments P
on C.customerNumber = P.customerNumber
Where amount > (select avg(amount) from payments);

# En el caso anterior, va realiar un calculo por cada registro.
# 1ra forma: Podemos optimizar, para que no se vuelva a calcular avg(amoung) seria crear una vista
# seleccionar ese lugar en el campo calculado, con la vista se evitaria calcular por cada 
# registro. 
-- 2da forma: avg como un campo mas, como una columna al costado y haria where amoung > avg_amount [agregar a la derecha de la tabla].
-- seria un join con cada uno de los datos, y comparar entre columnas. 
-- cuando hacemos calculos sobre otros campos, lo ideal es hacerlo una sola vez. 
-- 

# 2da forma :
Select C.customerNumber, C.customerName, amount
From (select *
From customers Where city = "Paris") C inner join payments P
on C.customerNumber = P.customerNumber
join (select avg(amount) as avg_amount from payments) AV
Where amount > avg_amount;

/*
PREGUNTA3: 
De los pagos posteriores al 15 de enero del 2005. Para una campaña de Marketing, nos solicitan los siguientes datos:
- Nombres
- Apellidos
- Teléfono
- Suma total de pagos
Asimismo solo se considerarán a aquellos clientes cuyos montos acumulados sean mayores en un 20% al promedio.
*/

select customers.customerName, customers.contactLastName, customers.phone, PD.total 
from (select SUM(amount) as total, customerNumber 
		from payments 
        WHERE datediff(paymentDate, "2005-01-15") > 0 
        group by customerNumber 
        HAVING total > (SELECT  1.20 * AVG(amount) 
						FROM payments)) PD 
inner join customers 
on customers.customerNumber = PD.customerNumber
limit 15;


/*
PREGUNTA4: Listar a los empleados (nombre y apellido) que pertenezcan a 
oficinas cuyo número de teléfono finalice en 0. Junto a los datos de 
los empleados también indicar los siguientes datos de la oficina:
- Dirección completa (en base a los campos addressLine1 y addressLine2)
- Número de teléfono.
Ejemplo:
*/
-- debemos ver que campo IFNULL

SELECT lastName, firstName, 
concat(addressLine1," ", IFNULL(addressLine2, " ")) as DireccionCompleta, 
phone
FROM employees E INNER JOIN offices O
ON E.officeCode = O.officeCode
WHERE phone LIKE '%0';

/*
PREGUNTA5: 
Queremos obtener los siguientes datos de órdenes:

- Nombre del cliente (customerName)
- Nombre del producto
- Precio x unidad del producto
- Comentarios de la venta
- Que cumplen las siguientes condiciones:

La venta debe haberse hecho posterior al 01 de enero del 2005.
Dentro de los comentarios debe estar la palabra "Customer".
El precio de la unidad debe ser mayor a 180.
*/


/*
PREGUNTA6: Queremos conocer los siguientes datos de algunas órdenes:

- Nombre del producto.
- Cantidad ordenada.
- Precio total (cantidad * precio unitario).

Solo se considerarán órdenes cuyo estado sea "Disputed". Asimismo 
el ordenamiento se hará en base al precio total de mayor a menor.
*/

SELECT P.productName, OD.quantityOrdered , (OD.quantityOrdered * OD.priceEach) as PrecioTotal
FROM products P
INNER JOIN orderdetails OD
ON P.productCode = OD.productCode
INNER JOIN orders O
ON OD.orderNumber = O.orderNumber
WHERE O.status = "Disputed";

