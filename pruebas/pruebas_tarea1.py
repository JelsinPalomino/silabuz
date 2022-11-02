lista = list()

class Alumnos:
    def __init__(self):
        self.matricula = ( )
        self.nombre = (" ")
        self.edad = ( )
        self.carrera = (" ")

def menu ():
    seleccion = 0
    while seleccion !=4:
        print("Bienvenidos a la aplicacion de registro de alumnos de la escuela UGMEX")
        print("conchita v2.0")
        print("elija una de las opciones")
        print("-"*30)
        print("1.- Registrar el alumno")
        print("2.- Mostrar los alumnos registrados")
        print("3.- Buscar un alumno")
        print("4.- Salir")
        seleccion = int(input("Elija una opción: "))
        if seleccion == 1:
            registrar()
        elif seleccion ==2:
            mostrar()
        elif seleccion ==3:
            buscar()
        elif seleccion ==4:
            salir()

def registrar():
    print("Esta es la función de registro")
    alumno = Alumnos()
    alumno.matricula = int(input("Introduce la matricula: "))
    alumno.nombre = input("Introduce el nombre: ")
    alumno.edad = int(input("Introduce la edad: "))
    alumno.carrera = input("Introduce la carrera que cursa: ")
    lista.append(alumno)

def mostrar():
    print("Esta es la función para mostrar alumnos registrados")
    for alumno in lista:
        print(f"El alumno {alumno.nombre}, de matricula {alumno.matricula}, con edad {alumno.edad} que cursa la carrera de {alumno.carrera}")

def buscar():
    print("Esta es la función para buscar un alumno")
    busqueda = int(input("Ingrese la matricula: "))
    for alumno in lista:
        if alumno.matricula == busqueda or alumno.nombre == busqueda:
            print(alumno.nombre, "-" ,alumno.matricula, "-" ,alumno.edad, "-" ,alumno.carrera)

def salir():
    print("Gracias por usar nuestra aplicación")


menu()