# Definimos una función llamada 'colores' que acepta múltiples argumentos con *args
def colores(*args):
    # Imprimimos un mensaje utilizando los valores de los argumentos pasados
    print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

# Llamamos a la función 'colores' pasando dos colores como argumentos
colores("blanco", "azul")  # Se imprimirá: "El color azul es mi favorito. El color blanco tampoco está mal."

# Definimos una función llamada 'suma' que acepta múltiples argumentos con *args
def suma(*args):
    # Sumamos los dos primeros valores que se pasen como argumentos
    sumaf = args[0] + args[1]
    # Imprimimos el resultado de la suma
    print("El resultado de la suma es:", sumaf)

# Llamamos a la función 'suma' pasando dos números como argumentos
suma(13, 13)  # Se imprimirá: "El resultado de la suma es: 26"
