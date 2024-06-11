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
