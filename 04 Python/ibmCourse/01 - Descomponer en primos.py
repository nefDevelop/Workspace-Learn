def isPrimo(n):
    ntemp = n
    state = True
    
    while ntemp > 0:
        # Nos aseguramos que no sea el mismo ni uno.
        if ntemp == n or ntemp == 1:
            ntemp -= 1 
            continue
        else:
            if n % ntemp == 0:
                # Solo devolvemos False cuando encontramos que divide por otro.
                return False
            
            ntemp -= 1 
        
    return state

# Generamos una array de los primos menores al numero dado.
def arrayPrimos(n):
    narray = []
    
    while n > 1:
        if isPrimo(n):
            narray.append(n)
            # print (n)

        n -= 1   

    return narray

def descomponerNum (num):
    ntemp = num
    arrTemp = []

    arrprimos = arrayPrimos(num)
    # Si el numero dado es un primo, comprobamos y devolvemos directamente.
    if num in arrprimos:
        print ("El numero es primo.")
        return
    
    # Como no lo es, probamos por cada numero primo del array
    for i in arrprimos:
        # miramos el resto con cada primo hasta que deje de ser 0 y pasamos al siguiente primo.
        while (num % i == 0):
            arrTemp.append(i)
            num = num / i

    return arrTemp       


numeroPedido = int(input())
print (descomponerNum(numeroPedido))




