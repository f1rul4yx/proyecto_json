import json

# Cargar el fichero json
def leer_fichero(archivo):
    with open(archivo, 'rt') as archivo:
        archivo = json.load(archivo)
    return archivo

# Consulta 1: Listar información
def listar_informacion(diccionario):
    print("Las bibliotecas disponibles son:")
    for datos in diccionario:
        print(f"    - {datos['biblioteca']}")
    biblioteca_input = input("Introduce una biblioteca: ")
    print(f"Los libros que hay en la {biblioteca_input} son:")
    for datos in diccionario:
        if biblioteca_input == datos['biblioteca']:
            for libros in datos['libros']:
                print(f"    - {libros['titulo']}, escrito por {libros['autor']}. De {libros['genero']} y publicado en el {libros['año_publicacion']}")