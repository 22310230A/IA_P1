# Solicitar la edad al usuario y convertirla a entero
edad = int(input('¿Cuál es tu edad?\n'))

# Verificar si la edad ingresada es válida
if edad <= 0:
	print('Nadie puede tener esa edad.')# Se ejecuta si la edad es 0 o menor
elif edad >= 1 and edad < 18:
	print('Eres menor de edad.')# Se ejecuta si la edad está entre 1 y 18 años
elif edad >= 18 and edad <= 45:
	print("Eres mayor de edad")# Se ejecuta si la edad está entre 18 y 45 años
elif edad >= 18 and edad <= 100:
	print('Eres mayor de edad.') # Se ejecuta si la edad está entre 45 y 100 años
elif edad >= 100 and edad <= 120:
	print("Eres mayor de edad") # Se ejecuta si la edad está entre 101 y 120 años
else:
	print('Edad no válida.') # Se ejecuta si la edad es mayor a 120