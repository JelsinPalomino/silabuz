-- DIA 17
-- USUARIOS Y CONTROL DE ACCESOS

# Crear usuario
create user "nuevoUsuario"@"localhost" identified by "%123%";

# PARTE: Consultar los usuarios de mysql
Select *
From mysql.user;

Select User, authentication_string 
From mysql.user;

# usuario actual 
Select user();

# PARTE: DAREMOS PRIVILEGIOS - GRANT [brindar]
Grant all privileges on *.* to "nuevoUsuario"@"localhost";

Flush privileges; 
Restart;

# PARTE: ELIMINAMOS LOS USUARIOS
# Revocar todos los privilegios
Revoke All privileges, Grant option from "nuevoUsuario"@"localhost";

# Damos el privilegio del select
Grant Select On *.* to "nuevoUsuario"@"localhost";

# Queremos remover un privilegio
Revoke Select On *.* From "nuevoUsuario"@"localhost";

# otros ejemplos
grant insert on *.* to "nuevoUsuario"@"localhost";
revoke insert on *.* to "nuevoUsuario"@"localhost";

Flush privileges;    # reiniciar el modulo del servidor, para actualizar los privilegios
Restart;             # reiniciando el servidor, debemos tener cuidado de este comando

Create table test1;

# SIEMPRE TENER CUIDADO CON LA DOCUMENTACIÓN DE LA VERSION QUE SE ESTA TRABAJANDO
# Eliminar usuario
drop User "nuevoUsuario"@"localhost";
Flush privileges;    # reiniciar el modulo del servidor, para actualizar los privilegios
Restart;             # reiniciando el servidor, debemos tener cuidado de este comando

Select * 
From mysql.user;

# para mostrar privilegios
show grants for "root"@"localhost";

-- Para dar multiples permisos, se puede dar un rol y también darle multiples 
-- permisos
-- lo ideal seria leer la documentación de mysql
-- restart no se podra usar si no tenemos el permiso de shutdown

# COMBINANDO - EJEMPLO

Create user "nuevoUsuario"@"localhost" identified by "%123%";

drop user "nuevoUsuario"@"localhost";

Update mysql.user Set authentication_string = password('987654321')
Where user = "nuevoUsuario" and host = "localhost";

Set password for "nuevoUsuario"@"localhost" = "987654321";


# PARTE: MANEJO DE INDICES
/*
Index:
Unique:
Primary: 
Full text:
btree:
hash:
*/

use ejemplo;

create table palabras(
	id int primary key auto_increment,
    palabra varchar(100)
);

insert into palabras(palabra)
values
("Palabra1"),
("Palabra2"),
("Palabra3"),
("Palabra4");

Select *
from palabras;

Create fulltext index index_1
on palabras(palabra);

show index from palabras;

# NOTA: 
# En otros contextos son cada uno
# Indice: un puntero para mejorar, optimizar la consulta
# Cursor: linea por linea, un elemento por elemento 
# Generadores: a cada instruccion un elemento pero no se manipula, ahorra espacio por consumir menos espacio en la memoria
#              pero no tiene un mismo fin. | ahorro en consumo de memoria



# PARTE: FUNDAMENTOS DE MODELAMIENTO
# ------------------------------------

























