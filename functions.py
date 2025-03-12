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

# Consulta 2: Contar información
def contar_informacion(diccionario):
    print("Las bibliotecas disponibles son:")
    for datos in diccionario:
        print(f"    - {datos['biblioteca']}")
    biblioteca_input = input("Introduce una biblioteca: ")
    libros_count = 0
    prestamos_count = 0
    for datos in diccionario:
        if biblioteca_input == datos['biblioteca']:
            for libros in datos['libros']:
                libros_count += 1
                for prestamos in libros['prestamos']:
                    prestamos_count += 1
    print(f"En la {biblioteca_input} hay un total de {libros_count} libros y se han realizado un total de {prestamos_count} préstamos.")