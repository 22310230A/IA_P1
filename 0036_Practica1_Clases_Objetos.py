## JonathanBN
# Clases y objetos - Programación orientada a objetos con Python

# Definimos una clase llamada 'Usuario'
class Usuario:
    # Atributos de la clase con valores por defecto
    nombre = ''
    apellidos = ''

    # Método de la clase que imprime los datos del usuario
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Creamos una instancia de la clase 'Usuario'
usuario001 = Usuario()

# Asignamos valores a los atributos 'nombre' y 'apellidos'
usuario001.nombre = 'Enrique'
usuario001.apellidos = 'Barros Fernández'

# Llamamos al método 'imprime_datos()' para mostrar la información del usuario
usuario001.imprime_datos()
