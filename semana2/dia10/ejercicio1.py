class Figura:
    def __init__(self, nombre:str, area, coordenada_x, coordenada_y):
        self.nombre = nombre
        self.area   = area
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y

    def __del__(self):
        return None

    def mostrar_figura(self):
        area = self.coordenada_x * self.coordenada_y
        print(f"La figura se llama {self.nombre}, Tiene un area de {self.area} e inicia en las coordenadas {self.coordenada_x}, {self.coordenada_y}")

nombre = "Circulo"
area = 30.5
coordenada_x = -1
coordenada_y = 2

a = Figura(nombre, area, coordenada_x, coordenada_y)
print(a.mostrar_figura())