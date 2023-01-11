### Loops, bucles o ciclos ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continua")

# For

my_list = [27, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (27, 1.82, "Aitor", "Machado", "Aitor")

for element in my_tuple:
    print(element)

my_set = {"Aitor", "Moure", 27}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Aitor", "Apellido":"Machado", "Edad":27}

for element in my_dict:
    print(element)
    if element == "Apellido":
        break
    print("Se ejecuta")
else:
    print("El buble for para mi diccionaio ha finalizado")

print("La ejecución continua")

for element in my_dict:
    print(element)
    if element == "Apellido":
        continue
    print("Se ejecuta")
else:
    print("El buble for para mi diccionaio ha finalizado")