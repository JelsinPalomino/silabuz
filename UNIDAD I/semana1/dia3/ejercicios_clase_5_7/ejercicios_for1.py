# 1.- Realiza una tabla de multiplicar
number_begin = 1
number_end   = 11

for f in range(number_begin,number_end):
    for i in range(1,11):
        print(f'{f} x {i} = {i * f}')
    print("-"*20)