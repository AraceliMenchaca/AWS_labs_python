'''
Este script se queda con los aminoacidos de 1 al 24 de secuencia de aminoácidos. Esta secuencia es una 
cadena de 110 letras que representan los diferentes aminoácidos.
'''

import re

# Lee el archivo
with open('preproinsulin-seq-clean.txt', 'r') as file:
    data_clean = file.read()

# Corta la cadena para obtener aminoácidos

data1_24 = data_clean[:24] 
data25_54 = data_clean[24:55]
data55_89 = data_clean[55:90]
data90_110 = data_clean[90:111]

# Crea nuevas líneas dentro del archivo preproinsulin-seq-clean.txt

with open('preproinsulin-seq-aminoacids.txt', 'w') as file:
    file.write(data1_24 + '\n')
    file.write(data25_54 + '\n')
    file.write(data55_89 + '\n')
    file.write(data90_110 + '\n')

#print(f'Los aminoácidos del 1 al 24 son: {data1_24}')
#print(f'Los aminoácidos del 25 al 54 son: {data25_54}')
#print(f'Los aminoácidos del 55 al 89 son: {data55_89}')
#print(f'Los aminoácidos del 90 al 110 son: {data90_110}')