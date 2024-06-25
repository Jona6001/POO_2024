'''
5.- 
Crear una lista y un diccionario con el contenido de esta tabla: 

  ACCION              TERROR        DEPORTES
  MAXIMA VELOCIDAD    LA MONJA       ESPN
  ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
  RAPIDO Y FURIOSO I  LA MALDICION   ACCION

  Imprimir la informacion

'''
import os
os.system('clear')

# Crear una lista con los nombres de las categorías
categorias = ['ACCION', 'TERROR', 'DEPORTES']

# Crear un diccionario donde las claves son las categorías y los valores son las películas o programas correspondientes
tabla = {
    'ACCION': ['MAXIMA VELOCIDAD', 'ARMA MORTAL 4', 'RAPIDO Y FURIOSO I'],
    'TERROR': ['LA MONJA', 'EL CONJURO', 'LA MALDICION'],
    'DEPORTES': ['ESPN', 'MAS DEPORTE', 'ACCION']
}

# Imprimir la información
print("Tabla:")
print("------")
for categoria, peliculas in tabla.items():
    print(categoria + ":")
    for pelicula in peliculas:
        print("  -", pelicula)
    print()