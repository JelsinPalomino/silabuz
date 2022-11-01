def print_triangle():
  number = int(input("Ingrese el numero: "))
  if number < 1:
    print("numero invalido, ingrese un numero mayor que 0")
  elif(number == 1):
    print('*' * number)
  else:
    for number in range(number):
      print('*' * (number+1))
    for number in range(number-1, -1, -1):
      print('*' * (number+1))

print_triangle()