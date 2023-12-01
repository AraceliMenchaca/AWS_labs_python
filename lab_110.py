# Laboratorio 110 - Tipo de datos String

# EJERCICIO 1 - String
string_1 = 'This is a string.'
print(string_1)
print(type(string_1))

# EJERCICIO 2 - Concatenado
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# EJERCICIO 3 - Input Strings
name = input("What's your name? ")
print(name)

# EJERCICIO 4 - Formatear Output Strings
color = input("What's your favorite color? ")
animal = input("What's your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))