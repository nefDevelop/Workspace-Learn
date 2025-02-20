# Experimenta

# Crea una función log que acepte cualquier número de
# argumentos y los imprima por pantalla en una misma
# línea. La línea debe empezar con el prefijo ‘LOG: ’.

# Modifica la función log para que usuario pueda
# especificar cualquier prefijo que desee.

# Modifica la función log para que el prefijo tenga el
# valor por defecto ‘LOG: ’.

# Modifica la función log para que el usuario pueda
# establecer tanto prefijo como separador entre
# argumentos. Ambos deben pasarse sólo por los
# nombres (no por posición) ‘sep’ y ‘prefix’. No hace
# falta que estos tengan valor por defecto.

# Modfica la función log para que ahora ‘sep’ y ‘prefix’
# tengan un valor por defecto.

# Modifica la función log para que acepte el siguiente
# diccionario. Recuerda que hay que pasarlo
# desempaquetándolo con la sintaxis de doble
# asterisco (**).

# tipo [LOG - ERROR - INFO]
def log (**Kargs):

    match (Kargs["tipo"]):
        case "LOG":
            cadenaImprimir = "[ LOGS ] "
        case "ERROR":
            cadenaImprimir = "[ ERROR ] "
        case "INFO":
            cadenaImprimir = "[ INFO ] "
        case _:
            cadenaImprimir = "[ UNDEF ] "

    cadenaImprimir = cadenaImprimir + Kargs["mensaje"]

    print (cadenaImprimir)

input("""Que tipo de log grabamos? OPCIONES ([ERROR, LOG, INFO, NONE], "Mensaje entre comillas")""")

log (tipo = , mensaje = Kargs])
