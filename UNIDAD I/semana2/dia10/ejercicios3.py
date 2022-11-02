import pytest


def test_punto():
    coordenada_x = 5
    coordenada_y = 10
    punto = Punto(coordenada_x, coordenada_y)
    # assert punto.coordenada_x == 10 
    assert False


    
"""
coordenada_x = 5
coordenada_y = 6

punto1 = Punto(coordenada_x, coordenada_y)

print(punto1.mostrar_punto())
"""

class Punto :
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def mostrar_punto(self):
        print(f"El punto esta en ({self.coordenada_x}, {self.coordenada_y})")


class Figura:
    def __init__(self, nombre:str, area, coordenada_x, coordenada_y):
        self.nombre = nombre
        self.area   = area
        self.location = Punto(coordenada_x, coordenada_y)
        #self.coordenada_x = coordenada_x
        #self.coordenada_y = coordenada_y


    def __del__(self):
        return None

    def mostrar_figura(self):
        print(f"La figura se llama {self.nombre} \n Tiene un area de {self.area} \n y {self.location.mostrar_punto()}")


