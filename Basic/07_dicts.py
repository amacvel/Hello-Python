### Dictionaries ###

my_dict = dict()
my_other_dict = {}
print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Aitor", "Apellido":"Machado", "Edad":27, 1:"Python"}

my_dict = {
    "Nombre":"Aitor",
    "Apellido":"Machado",
    "Edad":27,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.82
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle amacvel"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Machado" in my_dict)
print("Apellido" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "amacvel")
print(my_new_dict)