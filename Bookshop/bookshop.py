DB = [{
    "id": "cf_1",
    "title": "El hombre bicentenario",
    "author": "Isaac Asimov",
    "genre": "Ciencia ficción"
},
{
    "id": "ne_1",
    "title": "Lobo de mar",
    "author": "Jack London",
    "genre": "Narrativa extranjera"
},
{
    "id": "np_1",
    "title": "El legado de los huesos",
    "author": "Dolores Redondo",
    "genre": "Narrativa policíaca"
},
{
    "id": "dc_1",
    "title": "El error de Descartes",
    "author": "Antonio Damasio",
    "genre": "Divulgación científica"
},
{
    "id": "dc_2",
    "title": "El ingenio de los pájaros",
    "author": "Jennifer Ackerman",
    "genre": "Divulgación científica"
},
{
    "id": "ne_1",
    "title": "El corazón de las tinieblas",
    "author": "Joseph Conrad",
    "genre": "Narrativa extranjera"
},
{
    "id": "dc_5",
    "title": "Metro 2033",
    "author": "Dmitri Glujovski",
    "genre": "Divulgación científica"
},
{
    "id": "dc_5",
    "title": "Sidharta",
    "author": "Hermann Hesse",
    "genre": "Narrativa extranjera"
},
{
    "id": "el_1",
    "title": "Andres Trapiello",
    "author": "Las armas y las letras",
    "genre": "Narrativa extranjera"
},
{
    "id": "aa_1",
    "title": "El poder del ahora",
    "author": "Ekhart Tolle",
    "genre": "Narrativa extranjera"
},
]

genre = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]

user = "0"

def menu ():
    print(" Bookshop ".center(50, "-"))
    print ("1. ISBN".center(50))
    print ("2. Autor".center(50))
    print ("3. Título".center(50))
    print ("4. Género".center(50))
    print ("5. Actualizar libro con ISBN fijo".center(50))
    print ("6. Eliminar un libro".center(50))
    print ("Q. Terminar programa".center(50))
    print ("-"*50)

def pretty_book (book):
    for k, v in book.items():
        print (f" {k}: {v}")

def look_for_ISBN (user):
    for book in DB:
        if book ["id"] == user:
            return book
    return None
def get_by_term (term, search_term):
    result = []
    for book in DB:
        if book[term].lower().find(search_term.lower()) >= 0:
                result.append (book)
    return result
# def get_by_term (term, search_term):
#     result = []
#     for book in DB:
#         if book[term] == search_term:
#                 result.append (book)
#     return result

def bookshop_DB_update (book):
    print ("Pulsa enter hasta llegar al campo que deseas modificar")
    for k,v in list(book.items())[1:]:
        user = input (f"{k}: ")
        if user: 
            book [k] = user

def book_remove_by_id (user):
    book_to_delete = look_for_ISBN (user)
    if book_to_delete:
        DB.remove(book_to_delete)



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
        
#         print (DB)

