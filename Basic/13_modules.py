### Modules ###

import my_module

my_module.sum_values(5, 3, 1)
my_module.print_value("Hola Python!")

from my_module import sum_values, print_value

sum_values(5, 3, 1)
print_value("Hola  Python!")

# Módulos del sistema

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as pi_value

print(pi_value)