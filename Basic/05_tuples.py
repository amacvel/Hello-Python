### Tuples ###

my_tuple = tuple()
my_other_tuple = ()


my_tuple = (27, 1.82, "Aitor", "Machado", "Aitor")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Aitor"))
print(my_tuple.index("Machado"))
print(my_tuple.index("Aitor"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "amacvel"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) name 'my_tuple' is not defined