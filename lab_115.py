# Laboratorio 115 - Bucles while & for

# EJERCICIO 1 - "while"

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# se importa la librería random

import random

# se genera un número random entre el 1 y el 10

number = random.randint(1, 10)

# track whether user guessed your number

isGuessRight = False

# to handle the game logic, create a while loop

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print(f"You guess {guess}. That is correct! You win!")
    else:
        print(f'You guess {guess}. Sorry, that isn’t it. Try again.')

'''
If the user has not guessed the correct answer, enter the loop.

Ask the user for a guess.

Is the guess the correct number?

If the correct guess, tell the user it was the correct guess and exit the loop.

If the wrong guess, tell the user it was the wrong guess and continue the loop.
'''