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

    def getDisponible(self):
        return self.disponible

    # Método agregar
    def nuevo(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn




# Creamos la clase biblioteca
class Biblioteca():

    # Creamos el constructor
    def __init__(self):
        # Creamos la lista donde se guardaran los objetos libros
        self.biblioteca = []  
    
    # Método agregar
    def agregar(self, libro):
        # Agregamos a la biblioteca el objeto libro
        self.biblioteca.append(libro)

    # Hacemos verificacion de que sean digitos, transformamos y retornamos
    def isValidIsbn(self, message="", isbn="0"):
        if isbn != "0":
            if (not str(isbn).isdigit() and not str(isbn).isnumeric()):
                return int(isbn)

        elif message != "":
            isbn = input(message)
        
            while (not str(isbn).isdigit() and not str(isbn).isnumeric()):
                isbn = input(message)

            return int(isbn)
    
        
    # Ejercicio • Valida que el ISBN ingresado exista en la lista antes de prestar o devolver un libro.
    def existIsbn(self, isbn):
        # self.isValidIsbn(isbn)

        for libro in self.biblioteca:
            print (libro.isbn)

            if (libro.isbn == int(isbn)):
                return True
        
        return False   
     
    # Método prestar
    def prestar(self, isbn):
        while (not self.existIsbn(isbn)):
            isbn = self.isValidIsbn("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in self.biblioteca:
            if (int(isbn) == libro.isbn and not libro.getDisponible()):
                libro.setDisponible(False)    
                print("Libro prestado con éxito.\n")
            else:
                print("Libro elegido no etaba en la biblioteca.\n")

    # Método devolver
    def devolver(self, isbn):
        while (not self.existIsbn(isbn)):
            isbn = self.isValidIsbn("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in self.biblioteca:
            if (int(isbn) == libro.isbn and not libro.getDisponible()):
                libro.setDisponible(True)
                print("Libro devuelto con éxito.\n")
            else:
                print("Libro elegido ya etaba en la biblioteca.\n")

    # Método buscar
    def buscar(self, isbn):
        while (not self.existIsbn(isbn)):
            isbn = self.isValidIsbn("Inserte un ISBN correcto o que exista en la biblioteca: ")
            
        for libro in self.biblioteca:
            if (int(isbn) == libro.isbn):
                print ("--- Libro: %s - Autor: (%s) - ISBN: %i - Disponible: %s" %(libro.titulo, libro.autor, libro.isbn, "Si" if libro.disponible else "No"))
     
    # Método mostrar FORMATO --> - El Quijote (Cervantes) - ISBN: 12345 - Disponible: Sí
    def mostrar(self):
        for i in self.biblioteca:
            #print (f"- {i.titulo} ({i.autor}) - ISBN: {i.isbn} - Disponible: {i.disponible}" )
            print ("--- %s (%s) - ISBN: %i - Disponible: %s" %(i.titulo, i.autor, i.isbn, "Si" if i.disponible else "No"))

    def isEmpty(self):
        if not self.biblioteca:
            return True
        else:
            return False


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


# Creamos la biblioteca donde se guardaran los objetos libros
biblioteca = Biblioteca()

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
        
        isbn = biblioteca.isValidIsbn("ISBN: ")    

        # Comprobamos que si ya existe el ISBN se elija otro
        while (biblioteca.existIsbn(isbn)):
            isbn = biblioteca.isValidIsbn("Ya existe. ISBN: ")    

        # Agregamos libro a biblioteca
        libro.nuevo(titulo, autor, isbn)
        biblioteca.agregar(libro)
        print("Libro agregado con éxito. \n")
        
    elif (str(opcion) == "2"): #prestar
        if biblioteca.isEmpty():
            print ("Biblioteca vacia.")
        else:
            isbn = biblioteca.isValidIsbn("Ingresa el ISBN: ")
            biblioteca.prestar(isbn)
            print("Libro prestado con éxito\n")
    
    elif (str(opcion) == "3"): #Devolver
        if biblioteca.isEmpty():
            print ("Biblioteca vacia.")
        else:
            isbn = biblioteca.isValidIsbn("Ingresa el ISBN: ")
            biblioteca.devolver(isbn)
        
    elif (str(opcion) == "4"): #Mostrar
        if biblioteca.isEmpty():
            print ("Biblioteca vacia.")
        else:
            biblioteca.mostrar()
        
    elif (str(opcion) == "5"): #Buscar
        if biblioteca.isEmpty():
            print ("Biblioteca vacia.")
        else:
            isbn = biblioteca.isValidIsbn("Ingresa el ISBN: ")
            biblioteca.buscar(isbn)


