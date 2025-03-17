import os
import functions



archivo = functions.leer_fichero("librerias.json")



opcion = functions.menu()
while opcion != 0:
    if opcion == 1:
        functions.listar_informacion(archivo)
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    elif opcion == 2:
        functions.contar_informacion(archivo)
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    elif opcion == 3:
        functions.buscar_o_filtrar_informacion(archivo)
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    elif opcion == 4:
        functions.buscar_informacion_relacionada(archivo)
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    elif opcion == 5:
        functions.ejercicio_libre(archivo)
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    else:
        print("Esa opción no existe!!!")
        input("Pulsa una tecla para continuar...")
        os.system("clear")
    opcion = functions.menu()