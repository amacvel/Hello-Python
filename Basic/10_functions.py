### Functions ###

def my_function ():
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Machado", name = "Aitor")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Aitor", "Machado", "amacvel")
print_name_with_default("Aitor", "Machado")

def print_upper_texts (*texts): # * Parámetros dinámicos del mismo tipo
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "Python", "amacvel")