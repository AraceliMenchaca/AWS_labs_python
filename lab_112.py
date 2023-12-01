# Laboratorio 112 - Categorización de valores

# EJERCICIO 1 - Creating a mixed-type list

mixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in mixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))