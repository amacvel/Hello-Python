### Operadores aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # División con el resto #
print(10 // 3) # División que redondea al entero #
print(2 ** 3) # Exponencial

print("Hola " + "Python " + "¿Qué tal?")
# print("Hola " + 5) Falla, solo se puede concatenar string con string #
print("Hola " + str(5)) # Forzamos el cambio de dato para que se pueda concatenar #
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float)) # Forzamos el cambio de dato para que se pueda operar #

### Operadores comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("bbbb")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

### Operadores lógicos ###

print(3 > 4 and "Hola" > "Python") # False y False = False #
print(3 > 4 or "Hola" > "Python") # False o False = False #
print(3 < 4 and "Hola" < "Python") # True y True = True #
print(3 < 4 or "Hola" > "Python") # True o False = True #
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # True o (False y True = False) = True #
print(not(3 > 4)) # No falso se convierte en True #