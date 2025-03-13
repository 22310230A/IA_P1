class Usuario:
    # Constructor de la clase Usuario
    def __init__(self, nombre):
        self.nombre = nombre

    # Método para mostrar el nombre del usuario
    def mostrar_nombre(self):
        print("Nombre del usuario:", self.nombre)

# Crear una instancia de la clase Usuario
usuario1 = Usuario("Carlos")

# Mostrar el nombre del usuario
usuario1.mostrar_nombre()

# Eliminar el objeto usuario1
del usuario1.self

# Intentar acceder a usuario1 después de eliminarlo (esto generará un error si lo intentas ejecutar)
# usuario1.mostrar_nombre()
