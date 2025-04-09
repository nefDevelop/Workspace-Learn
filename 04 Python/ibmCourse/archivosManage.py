# Crear un archivo
fileName = './file.txt'

# abrir archivo en escritura
archivo = open(fileName, "w")
archivo.write("Hola archivo \n")
archivo.write("Es un archivo creado en python. ")

archivo.close()

def flads (a):
    num = a + a**4

