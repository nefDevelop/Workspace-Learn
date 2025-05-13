# Crear un archivo
fileName = './file.txt'

# Con with, no hace falta close
with open(fileName, 'w') as archivo:
    # abrir archivo en escritura
    archivo.write("Hola archivo \n")
    archivo.write("Es un archivo creado en python. ")

# Con try except
try: 
    with open(fileName, 'x') as archivo:
        archivo.write("Escritura modo exclusiva")
    print ("Creado")
except FileExistsError as e:
    print ("Archivo ya existe") 
    print (f"Detalle del error", e)
    
# Leer un archivo con readlines
with open(fileName, 'r') as archivo:
    # leer archivo
    contenido = archivo.readlines()
    print (contenido)
    
 