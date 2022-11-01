"""
funciones que añaden funcionalidad a otras funciones

"""
# Función decorador
def funcion_decoradora(funcion_parametro):
    #programar aquellas funcionalidades que deseamos darle a nuestras funciones
    def funcion_interior(*arg):
        print("realizar el calculo")
        funcion_parametro(*arg)
        # termino
        print("hemos terminado el calculo")
    return funcion_interior

@funcion_decoradora
def sum(num1, num2, num3):
    print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
    print(num1-num2)


