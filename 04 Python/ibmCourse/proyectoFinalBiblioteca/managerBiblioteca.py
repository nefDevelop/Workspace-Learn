import string

# 1. Clase Libro:
# • Crea una clase Libro con los atributos titulo (str), autor (str), isbn (str) y disponible (bool, inicialmente True).
# • Incluye un método agregar() que permita introducir un nuevo libro con sus características. 
# • Incluye un método prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado.
# • Incluye un método devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
# • Incluye un método mostrar()  que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no.
# • Incluye un método buscar() que busque un libro en concreto por su ISBM y lo muestre en pantalla con todos sus datos y diga si está disponible o no.

# Creamos la clase libro
class Libro: 
    
    # Definimos el constructor aceptando titulo como str, autor como str, isbn como str y displonible como booleano.
    def __init__():
        pass

    # Método agregar
    def agregar():
        pass

    # Método prestar
    def prestar():
        pass
    
    # Método devolver
    def devolver():
        pass
    
    # Método mostrar
    def mostrar():
        pass
    
    # Método buscar
    def buscar():
        pass
    


# 2. Gestión del inventario: 
# • Usa una lista para almacenar objetos de la clase Libro.
# • Implementa un bucle que permita al usuario interactuar con el programa mediante un menú con las siguientes opciones: 
# • a) Agregar un nuevo libro ingresando título, autor e ISBN.
# • b) Prestar un libro buscando por ISBN.
# • c) Devolver un libro buscando por ISBN.
# • d) Mostrar todos los libros y su estado (disponible o no).
# • e) Salir del programa.

# Crear menú
def showMenu():
    
    # Generamos la estructura del menu
    print ("\nBienvenido al Sistema de Gestión de Biblioteca\n")
    print ("1. Agregar libro.")
    print ("2. Prestar un libro.")
    print ("3. Devolver un libro.")
    print ("4. Mostrar todos los libros.")
    print ("5. Buscar un libro.")
    print ("6. Salir.\n\n")
    
    # cogemos la opcion
    opcion = input("Elige una opción: ")
    
    # Mediante recursividad, comparamos si opcion es válido. De no serlo, llamamos al menu. Si es válido, devolvemos valor.
    if (opcion.isdigit() == False):
            print("\nPor favor, ingrese una opción correcta. \n")
            showMenu()    
    else:
        opcion = int(opcion)      
        if (opcion < 1 or opcion > 6):
            print("\nPor favor, ingrese una opción correcta. \n")
            showMenu()
        else:
            return str(opcion)

    
# 3. Condiciones:
# • Valida que el ISBN ingresado exista en la lista antes de prestar o devolver un libro.
# • Si el usuario ingresa una opción inválida en el menú, muestra un mensaje de error y vuelve a pedir una opción. 


# Entregable:
# • Un script en Python que implemente todas las funcionalidades descritas.
# • El código debe ser claro, con comentarios explicativos y usando buenas prácticas.
# Ejemplo de uso. Al ejecutar el programa el resultado debería ser como se ve en el siguiente ejemplo:

# Bienvenido al Sistema de Gestión de Biblioteca
# 1. Agregar libro
# 2. Prestar libro
# 3. Devolver libro
# 4. Mostrar libros
# 5. Buscar
# 6. Salir

# Elige una opción: 1

# Título: El Quijote
# Autor: Cervantes
# ISBN: 12345
# Libro agregado con éxito.

# Elige una opción: 4
# - El Quijote (Cervantes) - ISBN: 12345 - Disponible: Sí

# Elige una opción: 2
# Ingresa el ISBN: 12345
# Libro prestado con éxito.

# Elige una opción: 4
# - El Quijote (Cervantes) - ISBN: 12345 - Disponible: No

# Consideraciones a tener en cuenta:
# Se creará la clase:
# • Libro
# Con los atributos:
# • Titulo
# • Autor
# • isbn
# • disponible
# Se crearán los métodos:
# • agregar
# • prestar
# • devolver
# • Mostrar
# • buscar

# El ejercicio se entregará en un solo archivo con extensión .py
# El nombre de la clase, atributos y métodos será exactamente el que se pide en el enunciado.
# Solo se admitirá una sola subida por alumno. En el caso de que un alumno suba más de una versión del ejercicio, solo se calificará la primera que se subiese, ignorando el sistema las demás. Por lo que se recomienda encarecidamente que se revisen detalladamente los ejercicios antes de proceder a su entrega. 
# Cualquier ejercicio que no cumpla escrupulosamente los requisitos pedidos NO SERÁ CORREGIDO.
# Todo aquel ejercicio que sea entregado posteriormente a las 00:00 horas del día no será corregido por el sistema.

# Creamos la lista donde se guardaran los libros
biblioteca = []


# Realizamos un bucle do while, obligamos a entrar la primera vez con la variable
opcion = "1"

# Entra y no ponemos if de opcion seis, el condicional del bucle hace su funcion.
while (opcion != "6"):
    
    # mostramos menu y guardamos seleccion que devuelva
    opcion = showMenu()
    
    if (opcion == "1"):
        pass
    elif (opcion == "2"):
        pass
    elif (opcion == "3"):
        pass
    elif (opcion == "4"):
        pass
    elif (opcion == "5"):
        pass


