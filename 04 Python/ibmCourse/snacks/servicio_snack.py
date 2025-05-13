import os.path
from snack import Snack


class servicioSnacks ():
  NOMBRE_ARCHIVO = 'snacks.txt'
  
  def __init__(self):
    self.snacks = []
    if os.path.isfile(self.NOMBRE_ARCHIVO):
      self.snacks = self.obtener_snacks()
      
    else:
      self.cargar_snacks_iniciales()
      
      
  def obtener_snacks(self):
    snacks = []
    try:
      with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
        for linea in archivo:
          _, nombre, precio = linea.strip().split(',')
          snack = Snack(nombre, float(precio))
          snacks.append(snack)
          
    except Exception as e:
      print (f'Error cargando archivo: {e}')
    return snacks
      
  def cargar_snacks_iniciales(self):
    snacks_iniciales = [ Snack('Papas', 70), 
                         Snack('Refresco',20), 
                         Snack('Sandwich', 100)]
    
    self.snacks.extend(snacks_iniciales)
    self.guardar_snacks_archivo(snacks_iniciales)
    
  def guardar_snacks_archivo(self, snacks):
    try:
      with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
        for snack in snacks:
          archivo.write(f'{snack.escribir_snack()}\n')
    except Exception as e:
      print(f'Error al guardar {e}')
      
  def agregar_snacks(self, snack):
    self.snacks.append(snack)
    self.guardar_snacks_archivo([snack])
    
  def mostrar_snacks(self):
    print('--- Snacks en el inventario ---')
    for snack in self.snacks:
      print (snack)
      
  def get_snacks (self):
    return self.snacks
      