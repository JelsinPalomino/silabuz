"""
Inicialice dos enteros: a = 0 y b = 10. 
Escriba un bucle que muestre e incremente 
el valor de a siempre que permanezca más 
bajo a la de b. Escriba otro bucle que disminuya 
el valor de b y muestre su valor si es impar. 
Iterar hasta que sea menor que 1.

"""

a=0
b=10
num=0
for num in range(a,b+1):
    print(num)
    a+=a


#   disminuye

for num in range(b-1,-1,-1):
    if num %2==1:
        print(num , 'es impar')
    else:
        print(num)
    a+=a
