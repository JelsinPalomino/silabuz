msg = ""
lista_invitados = []

while True:
    invitado = input("Ingrese el nombre del invitado:")
    regalo = input("¿Ha traido regaldo? <S/N>")
    if regalo.upper()=="S":
        lista_invitados.append(invitado)
    msg = input("Desea agregar otro invitado: <S/N>:")
    if msg.upper()=="N":
        break

print("lista de invitados")
print(f"Lista de invitados {lista_invitados}")