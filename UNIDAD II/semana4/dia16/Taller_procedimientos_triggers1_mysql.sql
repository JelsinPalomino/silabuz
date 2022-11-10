/*
EJEMPLO DEL TALLER - SOBRE LA BASE CLASSICMODELS
Tengo una orden, o venta. 
Si hago una venta, debo disminuir la venta en el stock // se debe hacer un procedimiento de almacenado

*/


use classicmodels;

Delimiter $$
Create trigger udp_qs after insert on orderdetails
	for each row
    begin 
		update products set quantityInStock = quantityInStock - New.quantityOrdered
			Where productCode = New.productCode;
    end; $$
Delimiter ;

Select * from orderdetails where productCode = "S10_678";

Select * from orderdetails where productCode = "S10_678";

Select * from orderdetails;

# Consultar los productos que no tienen ninguna orden
Select P.productCode, P.productName, OD.quantityOrdered, P.quantityInStock
from products P left join orderdetails OD 
on P.productCode = ifnull(OD.productCode, " ")
where quantityOrdered is null;


insert into orderdetails
values
(10143, "S18_1749", 12, 33.3, 4);

Select quantityInStock from products where productCode = "S18_1749";






