'''
Este script limpia el archivo preproinsulin-seq.txt de los elementos:
ORIGIN
//
espacios en blanco
saltos de linea o retornos

Todo esto usando "regex" para después separarlos con 
'''

import re

# Lee el archivo
with open('preproinsulin-seq.txt', 'r') as file:
    data = file.read()

# Elimina la línea que contiene "ORIGIN"
data = re.sub(r'ORIGIN.*\n', '', data)

# Elimina números en la línea de "ORIGIN"
data = re.sub(r'\d', '', data)

# Elimina las dos barras inclinadas "//"
data = data.replace('//', '')

# Elimina espacios en blanco y saltos de línea
data = re.sub(r'\s', '', data)

# Verifica que el archivo tenga 110 caracteres
if len(data) == 110:
    print("El archivo ahora tiene 110 caracteres.")
else:
    print("El archivo no tiene 110 caracteres.")

# Escribe el resultado de vuelta al archivo
with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(data)

