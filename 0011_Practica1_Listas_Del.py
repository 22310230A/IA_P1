# Definir una lista de colores
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
del colores[1]# Eliminar el segundo elemento (índice 1 → 'azul')
del colores[3]# Eliminar el cuarto elemento después de la primera eliminación (nuevo índice 3 → 'marrón')
del colores[-4]# Eliminar el cuarto elemento contando desde el final (índice -4 → 'negro')
del colores[-3]# Eliminar el tercer elemento contando desde el final (nuevo índice -3 → 'rosa')
# Imprimir la lista después de las eliminaciones
print(colores)