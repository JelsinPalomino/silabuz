Use classicmodels;

/*
Listar los vehiculos cuyo modelo de año sea de la decada
de los 60s. Ordenar los resultados del más caro al más economico.
*/
Select *
From products
Where productName Like "__6_%"
Order by buyPrice Desc
;

/*
Listar los vehiculos PickUp y ordenarlos por precio
desde el mas economico al de mayor precio
*/
Select *
From products
Where productName Like "%Pickup%"
Order by buyPrice Asc;
