import os.path

class ServicioPeliculas:
  NOMBRE_ARCHIVO = "peliculas.txt"
  
  def __init__(self): # Constructor de la clase serviciopeliculaes
    self.videoteca = []
    if os.path.isfile(self.NOMBRE_ARCHIVO):
      self.videoteca = self.recargarDatos()
    else:
      print(f"No existe, creando, videoteca")

      
  def recargarDatos(self): 
    # Cargamos los datos del archivo
    try:
        with os.open(self.NOMBRE_ARCHIVO,'r') as archivo:
          for line in archivo:
            pelicula = line.strip()
            if pelicula:
              self.videoteca.append(pelicula)
        
        return self.videoteca
    
    except FileNotFoundError as e:
        print(f'Mensaje: {e}')
        return []
    
    except Exception as e:
        print(f'Mensaje: {e}')
        return []
  
  def guardar_datos (self): #Metodo que guarda los datos en el archivo .txt
    try:
        with open(self.NOMBRE_ARCHIVO,'w') as archivo:
            for pelicula in self.videoteca:
                archivo.write(f'{pelicula}\n')
        
    except Exception as e:
        print(f'Mensaje: {e}')
  
  def buscar_peliculas (self): #Metodo que busca pelis en el archivo .txt
    try:
        pelicula = input("Ingrese el nombre de una película: ") #Pedir
        
    except Exception as e:
        print(f'Mensaje: {e}')

  
  
  def agregar_pelicula (self):
    pelicula = input("Ingrese el nombre de una película: ") #Pedir al usuario que ingrese un titulo para la peliulas.
    
    
  def listar_peliculas ( self ) : #Metodo lista las pelis guardadas en archivo .txt  
    pass
  
  def eliminar_peliculas (self):
    pass
