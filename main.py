import functions



archivo = functions.leer_fichero("librerias.json")



opcion = functions.menu()
while opcion != 0:
    if opcion == 1:
        functions.listar_informacion(archivo)
    elif opcion == 2:
        functions.contar_informacion(archivo)
    elif opcion == 3:
        functions.buscar_o_filtrar_informacion(archivo)
    elif opcion == 4:
        functions.buscar_informacion_relacionada(archivo)
    elif opcion == 5:
        functions.ejercicio_libre(archivo)
    else:
        print("Esa opción no existe!!!")
    opcion = functions.menu()