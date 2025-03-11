# Proyecto JSON: Gestión de Bibliotecas

Este proyecto consiste en extraer información de un archivo JSON que contiene datos sobre bibliotecas, libros y préstamos. A continuación, se describen los enunciados de las funciones que se implementarán:

1. **Listar información**: Listar todos los libros disponibles en las bibliotecas, mostrando su título, autor, género y año de publicación.
2. **Contar información**: Contar y mostrar el número total de libros en cada biblioteca, así como el número de préstamos realizados en cada una.
3. **Buscar o filtrar información**: Permitir al usuario ingresar un género literario y mostrar todos los libros de ese género, junto con la biblioteca en la que se encuentran.
4. **Buscar información relacionada**: Pedir al usuario el nombre de un autor y mostrar todos los libros escritos por ese autor, junto con la biblioteca en la que se encuentran y los usuarios que han solicitado préstamos de esos libros.
5. **Ejercicio libre**: Permitir al usuario ingresar un rango de años y mostrar todos los libros publicados en ese período, junto con la biblioteca en la que se encuentran y el número de préstamos que han tenido.

## Archivo JSON

El archivo JSON utilizado en este proyecto contiene datos de 3 bibliotecas, 15 libros por biblioteca y 5 préstamos por libro. La estructura del JSON es la siguiente:

- **Biblioteca**: Nombre de la biblioteca.
- **Libros**: Lista de libros con detalles como título, autor, género, año de publicación y disponibilidad.
- **Préstamos**: Lista de préstamos asociados a cada libro, con detalles como usuario_id, nombre_usuario, fecha_prestamo y fecha_devolucion.

## Instrucciones de uso

1. Clona este repositorio.
2. Ejecuta el archivo Python para probar las funciones.
