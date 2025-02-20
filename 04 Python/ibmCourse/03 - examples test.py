import random

## Ejercicio 1 - Sacar menor

a = -1
b = -4

if (a < b):
    print (a)
else :
    print (b)
    
    

## Ejercicio 2 - Invertir palabras de una cadena
str = 'código de práctica de prueba de geeks'

cadena = str.split()

a = len(cadena)

str = ''
while a >= 0:
    str = str + cadena[a-1] + ' '
    a -= 1
        
print (str)

## Ejercicio 3 - Realizar una suma de los elementos de una tupla
test_tup = (3,6,9,23,8,5,8,9)

print (f"Esta es la tupla original {test_tup}")
print (f"Esta es la tupla sumada {sum(test_tup)}")



## 4. Escriba un código que calcule una lista de números proporcionados.
def sum_list(lista):
    a = sum(lista)
    
    return a

print (sum_list([3,6,9,23,8,5,8,9]))
    

## 5. Escriba un código que desordene al azar una lista.

lista = ['casa', 'compra', 'un', 'estudio','rojo']
random.shuffle(lista)
print (lista)


## 6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.

# def howGrita(archivo):
#     # coger palabra a palabra
#     f = open(archivo).read()
    
#     count = 0
    
#     for i in f:
#     # comprobar qie isUpper
#         if i.isupper():
#             count =+ 1
            
    
#     return count

# howGrita()



# 7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?

lista = [4, 6, 8, 1, 0, 2]
print (lista[-1])



# 8. Escriba un programa para producir la serie Fibonacci en Python.



# 9. Escriba un programa en Python para comprobar si un número es primo.



# 10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.



# 11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.


try:
    # a = 1/0
    raise ValueError('Represents a hidden bug, do not catch this')

except ZeroDivisionError:
    print ("Division por cero, tonto")
except ValueError:
    print ("Hola")
    
    
# 14. ¿Como se puede acceder al último índice de una lista?
# con la posicion -1


