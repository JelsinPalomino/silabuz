#Leer números del usuario hasta que el usuario ingrese el 0. Luego mostrar la suma de todos los números ingresados.

num1 = int(input("Ingrese su numero: "))
oldernum = num1
sum = 0

while num1 != 0:
    num1 = int(input("Ingrese su numero: "))
    sum = sum + num1
print(f'La suma de los numeros digitados hasta el 0 es: {sum + oldernum}')