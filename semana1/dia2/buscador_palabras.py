##CONTADOR DE PALABRAS

frase = """
Me importan más ellos que yo mismo, y no permitiré que nadie los lastime.
Por eso nunca me rendiré, ¡te detendré, así tenga que matarte! Me salvaron de mí mismo,
me rescataron de la soledad, fueron los primeros que me aceptaron por quien soy.
Son mis amigos.
"""
print (frase)
wordsearch=input('Ingrese la palabra que quiere buscar en el texto anterior: ')
listFrase = frase.split()

frecuenciaPalab = []
count = 0
for palabras in listFrase:
    if wordsearch == palabras:
        count +=1
print(f"La palabra: '{wordsearch}' se repite {count} veces")
