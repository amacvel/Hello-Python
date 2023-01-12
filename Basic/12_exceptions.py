### Exceptions Handling ###

number_one = 5
number_two = 1
number_two = "1"

# try except

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# try except (obligatorios) else finally (opcionales)

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecución continua")

# Excepciones por tipo

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except ValueError as error: # No se cumple
    print(error)
except Exception as random_error:
    print(random_error)