"""
listAnidada=[[1,2,3],[4,5],[6,7,8,9]]

def imprime_lista_anidada_1(lisParam):
    listaCaracter=''
    for listaMayor in lisParam:
        for ListaMenor in listaMayor:
            listaCaracter+=str(ListaMenor)+ ' '
    print(listaCaracter)

imprime_lista_anidada_1(listAnidada)
"""

L = [500,100,200,300,200,100,600,400,800,400,500,900]
def elimina_duplicados(l):
    not_duplicated = set()
    for i in l:
        not_duplicated.add(i)
    return print(not_duplicated)
print("Forma 01")
elimina_duplicados(L)