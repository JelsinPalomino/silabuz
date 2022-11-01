"""
class Alumno:

    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        "Imprime un saludo en pantalla."
        print(f"¡Hola, {self.nombre}!")


alumno = Alumno("Pablo")
alumno.saludar()
"""

"""
Imagina que tienes la siguiente lista de valores 
[5, 1, 9, 2, 7, 4] y quieres saber si el número 2 
está contenido en dicha lista. La estructura típica 
de bucle while para ello es como sigue:
"""

valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')