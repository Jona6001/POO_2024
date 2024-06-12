#Funciones para las peliculas
lista_peliculas = []

def agregar_pelicula(nombre):
    lista_peliculas.append(nombre)
    print(f'Película "{nombre}" agregada.')

def remover_pelicula(nombre):
    if nombre in lista_peliculas:
        lista_peliculas.pop(nombre)
        print(f'Película "{nombre}" removida.')
    else:
        print(f'Película "{nombre}" no encontrada en la lista.')

def consultar_peliculas():
    if lista_peliculas:
        print("\nLista de películas:")
        for i in lista_peliculas:
         print(i)
    else:
        print("No hay películas en la lista.")

def buscar_pelicula(nombre):
    """Busca una película por nombre."""
    encontradas = [pelicula for pelicula in lista_peliculas if nombre.lower() in pelicula.lower()]
    if encontradas:
        print(f'Películas encontradas con el nombre "{nombre}":')
        for idx, pelicula in enumerate(encontradas, start=1):
            print(f'{idx}. {pelicula}')
    else:
        print(f'No se encontraron películas con el nombre "{nombre}".')

def vaciar_lista():
    """Vacía la lista de películas."""
    lista_peliculas.clear()
    print("Lista de películas vaciada.")