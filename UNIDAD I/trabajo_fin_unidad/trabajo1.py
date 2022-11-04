"""
Tarea 1: Programa en Python para registrar libros

"""
import csv


def open_csv():
    with open("libros.csv", "r", encoding='utf-8') as f:
        book = csv.reader(f)
        books = [row for row in book] 
        print(books)
    return books

class Libro:
    def __init__():
        self.id = (' ')
        self.titulo = (' ')
        self.genero = (' ')
        self.isbn = (' ')
        self.editorial = (' ')
        self.autor = (' ')

    
def menu():
    



    def show_books(self, books):
        print(books)
        libros = [row[1] for row in self.books]
        print(libros)

    

q = Libro()
q.open_csv()
q.show_books()

