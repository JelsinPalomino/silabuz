def power(x, y):
    if y == 0:
        return 1
    if y >= 1:
        return x * power(x, y - 1)


def ejemplo1():
    while True:
        try:
            num1 = int(input("ingrese el primer numero\n"))
            break
        except ValueError:
            print("debe ingrese un numero\n")
            continue
    while True:
        try:
            num2 = int(input("ingrese el segundo numero\n"))
            break
        except ValueError:
            print("debe ingrese un numero\n")
            continue

    operador = input('Ingrese el operador: ')
    while operador not in ('+', '-', '*', '/', 'potencia'):
        print('Ingresa un operador válido')
        operador = input('Ingrese el operador: ')

    if (operador == '+'):
        resultado = num1 + num2
    elif (operador == '-'):
        resultado = num1 - num2
    elif (operador == '*'):
        resultado = num1 * num2
    elif (operador == '/'):
        resultado = num1 // num2
    elif (operador == 'potencia'):
        resultado = power(num1, num2)

    print('el resultado es: ', resultado)


ejemplo1()


print("HOla mundo")
print("Como estan")