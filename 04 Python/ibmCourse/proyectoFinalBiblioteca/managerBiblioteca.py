#import string


# Creamos la clase libro
class Libro(): 
    
    # Definimos el constructor aceptando titulo como str, autor como str, isbn como str y displonible como booleano.
    def __init__(self):
        self.titulo = ""
        self.autor = ""
        self.isbn = ""
        self.disponible = True
        
    # Setter de Disponible
    def setDisponible(self, bool):
        self.disponible = bool

    # Método agregar
    def agregar(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        
        # Agregamos a la biblioteca el objeto libro
        biblioteca.append(self)

    # Método prestar
    def prestar(self, isbn):
        while (existIsbn(isbn) == False):
            isbn = input("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in biblioteca:
            if (int(isbn) == libro.isbn):
                libro.setDisponible(False)    
                # Libro prestado con éxito.
                    
    # Método devolver
    def devolver(self, isbn):
        while (existIsbn(isbn) == False):
            isbn = input("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in biblioteca:
            if (int(isbn) == libro.isbn):
                libro.setDisponible(True)         
  
    
    # Método mostrar FORMATO --> - El Quijote (Cervantes) - ISBN: 12345 - Disponible: Sí
    def mostrar(self):
        for i in biblioteca:
            #print (f"- {i.titulo} ({i.autor}) - ISBN: {i.isbn} - Disponible: {i.disponible}" )
            print ("- %s (%s) - ISBN: %i - Disponible: %s" %(i.titulo, i.autor, i.isbn, "Si" if i.disponible == True else "No"))

    # Método buscar
    def buscar(self, isbn):
        while (existIsbn(isbn) == False):
            isbn = input("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in biblioteca:
            if (int(isbn) == libro.isbn):
                print ("- Libro: %s - Autor: (%s) - ISBN: %i - Disponible: %s" %(libro.titulo, libro.autor, libro.isbn, "Si" if libro.disponible == True else "No"))
     

# Funcion para la eleccion del menu
def showMenu():
    # Bucle infinito hasta que el número sea correcto
    while True:
        
        # Cogemos opcion
        opcion = input("Elige una opción (1-6): ")
        
        # Si es digito y si es un numero del menu retornamos
        if (opcion.isdigit()):
            opcion = int(opcion)
            if (opcion >= 1) and (opcion <= 6):
                return opcion
        
        print("\nPor favor, ingrese una opción válida.\n")

    


# Hacemos verificacion de que sean digitos, transformamos y retornamos
def isValidIsbn(message):
    isbn = input(message)
   
    while (str(isbn).isdigit() == False):
        isbn = input(message)

    return int(isbn)
    
# Ejercicio • Valida que el ISBN ingresado exista en la lista antes de prestar o devolver un libro.
def existIsbn(isbn):
    for libro in biblioteca:
        # print (libro.isbn)

        if (libro.isbn == int(isbn)):
            return True
    
    return False    

# Creamos la lista donde se guardaran los objetos libros
biblioteca = []

# Generamos la estructura del menu que segun el ejemplo no hay que reiterar.
print ("\nBienvenido al Sistema de Gestión de Biblioteca\n")
print ("1. Agregar libro.")
print ("2. Prestar un libro.")
print ("3. Devolver un libro.")
print ("4. Mostrar todos los libros.")
print ("5. Buscar un libro.")
print ("6. Salir.\n\n")

# Realizamos un bucle do while, obligamos a entrar la primera vez con la variable
opcion = "1"

# Entra y no ponemos if de opcion seis, el condicional del bucle hace su funcion.
while (str(opcion) != "6"):
    
    # mostramos menu y guardamos seleccion que devuelva
    opcion = showMenu()
    
    if (str(opcion) == "1"): #Agregar
        # Creamos objeto Libro y cojemos los datos para agregar un libro nuevo
        libro = Libro()
        titulo = input("Título: ")
        autor = input("Autor: ")
        
        isbn = isValidIsbn("ISBN: ")    

        # Comprobamos que si ya existe el ISBN se elija otro
        while (existIsbn(isbn) != False):
            isbn = isValidIsbn("Ya existe. ISBN: ")    

        # Agregamos libro a biblioteca
        libro.agregar(titulo, autor, isbn)
        print("Libro agregado con éxito. \n")
        
    elif (str(opcion) == "2"): #prestar
        isbn = isValidIsbn("Ingresa el ISBN: ")
        libro.prestar(isbn)
        print("Libro prestado con éxito\n")
    
    elif (str(opcion) == "3"): #Devolver
        isbn = isValidIsbn("Ingresa el ISBN: ")
        libro.devolver(isbn)
        print("Libro devuelto con éxito.\n")
        
    elif (str(opcion) == "4"): #Mostrar
        libro.mostrar()
        
    elif (str(opcion) == "5"): #Buscar
        isbn = isValidIsbn("Ingresa el ISBN: ")
        libro.buscar(isbn)


