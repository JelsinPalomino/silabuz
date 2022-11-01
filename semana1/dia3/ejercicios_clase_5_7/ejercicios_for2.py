# Crea un bucle que cuente los numeros pares hasta el 100:

# Agregar validacion, que sea numero. 

def print_even_number():
  number = int(input("Ingrese el numero: "))
  
  for number in range(1, number+1):
    if number % 2 == 0:
      print(f"{number}")

print_even_number()