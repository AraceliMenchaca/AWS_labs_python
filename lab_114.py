# Laboratorio 114 - Condicionales

# EJERCICIO 1 - "if"
'''
userReply = input("Do you need to ship your package? (Enter yes or no) ")

if userReply == 'yes':
    print("We can help you ship that package!")


# EJERCICIO 2 - "else"
else:
    print("Please come back when you need to ship a package. Thank you.")

'''

# EJERCICIO 3 - "elif"

userRep = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, copy) ")

if userRep == 'stamps':
    print("We have many stamp designs to choose from.")
elif userRep == 'envelope':
    print("We have many envelope sizes to choose from.")
elif userRep == 'copy':
    copies = input('How many copies would you like? (Enter a number) ')
    print("Here are {} copies".format(copies))
else:
    print("Thank you, please come again.")

