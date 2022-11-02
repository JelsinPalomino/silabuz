"""
Queremos asegurar un recinto presurizado. Establecemos un umbral de presión 
y un umbral de volumen: pThreshold = 2.3, vThreshold = 7.41. Se le pide que
ingrese la presión y el volumen corriente del recinto y que escriba un guión
que simula el siguiente comportamiento: – si el volumen y la presión están 
por encima de los umbrales: parada inmediata; – si solo la presión es superior
al umbral de presión: solicite aumentar el volumen luz del altavoz; – si solo 
el volumen está por encima del volumen umbral: pida que disminuya el volumen 
del recinto; – si no declarar que “todo está bien”.

"""

pression_umbral = 2.3
volumne_umbral  = 7.41

pression_input = int(input("Ingrese la presion: "))
volumne_input  = int(input("Ingrese el volumen: "))

while pression_input != volumne_input:
    if pression_input > pression_umbral and volumne_input > volumne_umbral:
        break
    elif pression_input > pression_umbral:
        print(f"incremente el valor del volumen luz del altavoz")
    elif volumne_input > volumne_umbral:
        print(f"disminuya el volumen del recinto")
    else:
        print(f"todo esta bien")

    pression_input = int(input("Ingrese la presion: "))
    volumne_input  = int(input("Ingrese el volumen: "))

