"""
Leer nombre de invitados y agregarlos a una lista si han traido regalo
Tener la opcion de detener la adicion de invitados 
Finalmente imprimir los invitados que llevaron regalo
"""

# Maria
# ideal_agregar variables en ingles
# Entrada podria ser un booleano, flac_ [java], "is" generalmente usado [python]
# Para un arreglo, lst_[nombre], [nombre]s

entrada=False
invitados_regalo=[]
while not entrada:
    invitado=input('Ingrese nombre de invitado: ')
    regalo=input('Trajo regalo?, responda con (Y/N) ').upper()
    if regalo=='Y':
        invitados_regalo+=[invitado]
    continuar=input('Desea seguir agregando mas invitados? (Y/N)').upper()
    if continuar=='N':
        entrada=True

print(f'Trajeron relago {invitados_regalo}')
