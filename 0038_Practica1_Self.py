# Definimos la clase Usuario
class Usuario:
    # Método constructor (__init__) que inicializa los atributos de la instancia
    def __init__(self, nombre, apellidos):
        self.nombre = nombre  # Se almacena el nombre en el atributo de la instancia
        self.apellidos = apellidos  # Se almacena el apellido en el atributo de la instancia

    # Método para imprimir los datos del usuario
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

# Creamos un objetos (instancias) de la clase Usuario
usuario001 = Usuario('Josue', 'Gomez')


# Modificamos el atributo 'nombre' de usuario001
usuario001.nombre = 'Alejandro'

# Llamamos al método imprime_datos para mostrar los datos de usuario001
usuario001.imprime_datos()
