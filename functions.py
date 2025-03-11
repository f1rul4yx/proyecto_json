import json

# Cargar el fichero json
def leer_fichero(archivo):
    with open(archivo, 'rt') as archivo:
        archivo = json.load(archivo)
    return archivo