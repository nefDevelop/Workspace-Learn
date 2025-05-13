from servicio_snack import servicioSnacks
from snack import Snack

class Maquina_Snacks():
  
  def __init__(self):
    self.servicio_snacks = servicioSnacks()
    self.productos = []
    
  def maquina_snacks(self):
    salir = False
    print(' *** Maquina de Snacks *** ')
    self.servicio_snacks.mostrar_snacks()
    
    while not salir:
      try:
          opcion = self.mostrar_menu()
          salir = self.ejecutar_opcion(opcion)
      except Exception as e:
          print(f'Error maquina snacks: {e}')
          
  def mostrar_menu(self):
    print(f"""Menu:
          1. Comprar snack
          2. Mostrar ticket
          3. Agregar nuevo snack
          4. Inventario Snakcs
          5. Salir""")
    return int(input('Elige una opcion: '))
  
  def ejecutar_opcion(self, opcion):
    if opcion == 1:
      self.comprar_snack()
    elif opcion == 2:
      self.mostrar_ticket()
    elif opcion == 3:
      self.agregar_snack()
    elif opcion == 4:
      self.servicio_snacks.mostrar_snacks()
    elif opcion == 5:
      print(f"Regresa pront.")
      return True
    
    else: 
      print ('Opcion inválida')
      return False
    
    
  def comprar_snack(self):
    id_snack = int(input('Que snack quieres comprar (id)? '))
    snacks = self.servicio_snacks.get_snacks()
    snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
    
    if snack:
      self.productos.append(snack)
      print (f'Snack Encontrado: {snack}')
      
    else:
      print ('Id incorrecto')
    
  # muestra tiquet 
  def mostrar_ticket(self): 
    if not self.productos:
      print(f"No hay snacks en el ticket")
      return
    else:
      total = sum(snack.precio for snack in self.productos)
      print(f"Tiquet de productos")
      for producto in self.productos:
        print(f"\t- {producto.nombre} - ${producto.precio:.2f}")
      
      print(f"\tTotal: ${total:.2f}")
      
  def agregar_snack(self):
    nombre = input("Nombre del snack: ")
    precio = float(input("Precio del snack: "))
    nuevo_snack = Snack(nombre, precio)
    self.servicio_snacks.agregar_snacks(nuevo_snack)
    print(f"Snack Agregado con exito")
    
    
if __name__ == '__main__':
  maquina_snacks = Maquina_Snacks()
  maquina_snacks.maquina_snacks()