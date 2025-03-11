# Inicializar la variable x
x = 0

# Bucle while que se ejecuta mientras x sea menor que 30
while x < 30:
    # Verificar si x es uno de los valores que se deben saltar
    if x == 4 or x == 6 or x == 10:
        print(f'Se saltó el valor {x} de x')  # Imprime el mensaje de salto
        x += 1  # Incrementa x en 1 para continuar al siguiente valor
        continue  # Salta a la siguiente iteración del bucle sin ejecutar el resto del código
    
    # Imprimir el valor de x si no fue saltado
    print('El valor del bucle es:', x)
    
    # Verificar si x es igual a 15 para romper el bucle
    if x == 15:
        print(f'Se rompió la ejecución del bucle cuando x valía {x}')  # Mensaje cuando se rompe el bucle
        break  # Rompe la ejecución del bucle
    
    # Incrementar x en 1
    x += 1
