import re

def limpiar_y_dividir_secuencia(archivo_entrada, archivo_salida_limpio, archivo_salida_aminoacidos):
    # Lee el archivo de entrada
    with open(archivo_entrada, 'r') as file:
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

    # Escribe el resultado de vuelta al archivo limpio
    with open(archivo_salida_limpio, 'w') as file:
        file.write(data)

    # Corta la cadena para obtener aminoácidos
    data1_24 = data[:24]
    data25_54 = data[24:54]
    data55_89 = data[54:89]
    data90_110 = data[89:110]

    # Escribe los aminoácidos en el archivo de salida correspondiente
    with open(archivo_salida_aminoacidos, 'w') as file:
        file.write(data1_24 + '\n')
        file.write(data25_54 + '\n')
        file.write(data55_89 + '\n')
        file.write(data90_110 + '\n')

# Llama a la función con los nombres de los archivos
limpiar_y_dividir_secuencia('preproinsulin-seq.txt', 'preproinsulin-seq-clean.txt', 'preproinsulin-seq-aminoacids.txt')
