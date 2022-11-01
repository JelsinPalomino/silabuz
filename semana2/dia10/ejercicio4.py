"""
Cree la clase Rueda con los siguientes atributos:

Marca = Michelin
Índice de carga = 16
Diámetro = 99
Cree el método mostrar_llanta, que imprima lo siguiente:

La llanta es de marca "Marca"
El índice de carga es de "Índice de carga"
Y tiene un diámetro de "Diámetro"
Realice la composición con la clase Automovil.

Notas:

Utilice mostrar_llanta dentro del método tipo_carro
Utilice los datos del Problema 2
Cree un objeto automovil, use mostrar_llanta y luego elimine el objeto
"""


class Rueda:
    def __init__(self, marca:str, indice:float, diametro:int):
        self.marca = marca
        self.indice = indice
        self.diametro = diametro
    
    def mostrar_llanta(self):
        print(f"La llanta es de marca {self.marca} \n El índice de carga es de {self.indice} \n Y tiene un diámetro de {self.diametro}")

marca = "Michelin"
indice = 16
diametro = 99