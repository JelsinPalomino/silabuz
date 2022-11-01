"""
lista = ["paula", None, "flavia", None, "gabriela"]
nombres = [nombre.capitalize() if nombre is not None else "" for nombre in lista]
print(nombres)
"""

"""
#LAMBDA
area_rectangulo = lambda base, altura: base*altura

print(area_rectangulo(10,5))
"""
"""
def agregar_uno(num:int)->int:
    return num+1

print(agregar_uno(5))
"""
def adaptar(funcion):
    def funcion_auxiliar(a,b):
        if b!=0:
            return funcion(a,b)
        return("No podemos ejecutar division entre 0")
    return funcion_auxiliar