# import bookshop
# print (bookshop.DB)
#Otra forma de importar

#IMPORTANTE
#Debe ejecutarse primero el programa dentro de bookshop para que yo tenga mis variables definidas
#Todo va ordenado, si ahora importo random, me saldrá primero bookshop, porque lo he importado primero
#Cada vez que importamos nos traemos todo, lo ejecutamos, no solo traemos las variables
#Módulo creo que es el nombre que le damos al importar un fichero externo ejecutable

from bookshop import DB, menu, pretty_book, look_for_ISBN, get_by_term, bookshop_DB_update, book_remove_by_id

user = "0"
while user != "q":
    menu ()
    user = input ("")
    if user == "1":
        user = input ("ISBN: ")
        book_founded = look_for_ISBN (user)
        if book_founded:
            pretty_book(book_founded)
            print ("-"*30)
        else:
            print ("No se encuentra el libro con el ISBN {user}")
        input()
    elif user == "2":
        user = input ("Autor: ")
        books = get_by_term ("author", user)
        for book in books:
            pretty_book(book)
            print ("-"*30)
        input()
    elif user == "3":
        user = input ("Título: ")
        books = get_by_term ("title", user)
        for book in books:
            pretty_book(book)
            print ("-"*30)
        input()
 
    elif user == "4":
        user = input ("Género: ")
        books = get_by_term ("genre", user)
        for book in books:
            pretty_book(book)
            print ("-"*30)
        input()
    elif user == "5":
        user = input ("Modificar libro con este ISBN: ")
        updating_book_constant_id = look_for_ISBN (user)
        if updating_book_constant_id:
            bookshop_DB_update (updating_book_constant_id)
    elif user == "6":
        user = input ("Eliminar libro con ISBN: ")
        book_remove_by_id (user)

