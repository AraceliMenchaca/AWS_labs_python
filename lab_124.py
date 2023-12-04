# Laboratorio 124 - Uso de funciones para implementar un cifrado César

'''
In programming, a function is a named section of a program that performs a specific task. 
Python has built-in functions like print() that are provided by the language. 
Additionally, you can use functions provided by other developers through the import statement. 
For example, you can use import math if you want to use the math.floor() function. 
In Python, you can make your own functions, which are called user-defined functions.
'''

# EJERCICIO 1 - Creating a user-defined function

def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# EJERCICIO 2 - Encrypting a message

def getMessage():
    stringtoEncrypt = input('Please enter a message to encript: ')
    return stringtoEncrypt

# EJERCICIO 3 - Getting a decipher key

def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1 - 25): ")
    return shiftAmount

# EJERCICIO 4 - Encrypting a message

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# EJERCICIO 5 - Decrypting message

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# EJERCICIO 6 - Creating a main function

def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()