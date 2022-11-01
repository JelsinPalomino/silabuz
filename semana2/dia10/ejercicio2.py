from ejercicio4 import *

class Automovil:
    def _init_(self,marca, anio,placa, numero_asientos) :
        self.__marca=marca
        self.anio=anio
        self.placa=placa
        self.numero_asientos=numero_asientos
        self.rueda = Rueda()

    def set_rueda(self, marca, indice, diametro):
        self.rueda.marca    = marca
        self.rueda.indice   = indice
        self.rueda.diametro = diametro

    def get_marca(self):
        return self.__marca    
    def set_marca(self,marca):
        self.__marca=marca    
    
    def mostrar_carro(self):
        return f'El carro es de marca {self.__marca} del año {self.anio} Y tiene placa número {self.placa}'

    def tipo_carro(self):
        tipo=''    
        if self.numero_asientos>20:
            tipo='bus '
        elif self.numero_asientos>10:
            tipo='combi'
        else:
            tipo='carro'
        return f"{tipo} {self.rueda.mostrar_llanta()}"

