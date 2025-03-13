class Usuario:
    # Definimos el constructor __init__ que se ejecuta cuando creamos una instancia de la clase
    def __init__(self, nombre, apellidos):
        self.nombre = nombre  # Asignamos el valor de 'nombre' al atributo de la instancia
        self.apellidos = apellidos  # Asignamos el valor de 'apellidos' al atributo de la instancia

    # Definimos un método para imprimir los datos de la instancia
    def imprime_datos(self):
        print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)  # Imprimimos los atributos

# Creamos dos objetos (instancias) de la clase Usuario
usuario001 = Usuario('Josue',"Alejandro")


# Llamamos al método imprime_datos de cada objeto
usuario001.imprime_datos()  # Muestra los datos del usuario001

