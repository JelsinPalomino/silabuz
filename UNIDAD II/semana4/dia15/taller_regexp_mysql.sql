-- DIA 14: TALLER SOBRE REGEXP
-- 

/*
PREGUNTA 1: 
Seleccionar solo los campos: articleID, pubDate, headline, 
byline, keywords y snippet. Crear un expresión regular para el 
término: "Mr." (que hace referencia a Mister o señor), 
dicha expresión regular se ha de aplicar al campo headline
*/

use nyt_comments;
select articleID, pubDate, headlina, byline, keywords, snippet
from document_summary
where headline regexp "Mr";

/*
PREGUNTA2:
A la consulta anterior modificar la expresión regular para 
también considerar el término "Colbert".
*/

use nyt_comments;
select articleID, pubDate, headlina, byline, keywords, snippet
from document_summary
where headline regexp "Mr|Colbert";

/*
PREGUNTA3:
Seleccionar los campos: articleID, pubDate, headline, byline, 
keywords y snippet. Y crear una expresión regular para headline 
que permita filtrar registros que contengan el término "Russia" 
pero solo precedido de palabras que contengan alguno de estos 
caracteres: 1, 2, 3, A o a.
*/
select articleID, pubDate, headlina, byline, keywords, snippet
from document_summary
where headline regexp "[123Aa] Rusia";

/*
PREGUNTA4:
Seleccionar los campos: articleID, pubDate, headline, byline, 
keywords y snippet. Crear una expresión regular para snippet 
que permita filtrar registros que contengan "photo book" o "new book".
*/

select articleID, pubDate, headline, byline, keywords, snippet
from document_summary
where snippet regexp "(photo|new)+ book";

-- photo o new al menos uno de ellos debe estar en el comentario
-- "+" uno o muchos

/*
Full-text searching
Alterar los campos headline y snippet de la presente tabla para que sean FULLTEXT.
PREGUNTA5
Ejecutar los siguientes 3 bloques de código, analizar los 
resultados entre alumnos e indicar las diferencias.
*/

alter table document_summary add fulltext(headline);
alter table document_summary add fulltext(snippet);


# Analizar las sigueintes queries
SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("book" IN NATURAL LANGUAGE MODE);

SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("book" IN BOOLEAN MODE);

SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("book" WITH QUERY EXPANSION);

-- La frase concatenada
-- full text search, soporta query expansion. Hara la busqueda de la frase que 
-- estamos buscando de una manera concatenada, y encontrara la frase mas relevante
-- dos busquedas, doble busqueda
-- lo va tomar un termino y lo va buscar en el campo, y el segundo termino y agrupa  
-- 
-- 
-- 
-- 

/*
PREGUNTA.
De la pregunta anterior, encontrar la query que permita no 
tomar en consideración "new" en la búsqueda de book. 
Es decir, "new book" no debería ser considerado dentro de los 
resultados de la query.
*/
# Usaremos el modo Booleano
SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("book -new" IN BOOLEAN MODE);

SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("book -new" WITH QUERY EXPANSION);

/*
Deseamos adaptar la query para poder filtrar la frase new book, 
escriba la correspondiente consulta.
*/
-- comilla simple para que sea exactamente new book

SELECT articleID, pubDate, headline, byline, keywords, snippet 
FROM nyt_comments.document_summary
WHERE MATCH(snippet) AGAINST("'new book'" IN BOOLEAN MODE);

/*

*/







