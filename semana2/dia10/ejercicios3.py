import pytest


def test_punto():

    assert False


class Punto :
    def __init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def mostrar_punto(self):
        print(f"El punto esta en ({self.coordenada_x}, {self.coordenada_y})")
    

coordenada_x = 5
coordenada_y = 6

punto1 = Punto(coordenada_x, coordenada_y)

print(punto1.mostrar_punto())

