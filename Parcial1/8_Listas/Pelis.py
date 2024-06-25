#Ejemplo 5.- Crear un programa que permita gestionar (Administrar) peliculas colocar un menu de opciones
#para agregar, remover,consultar peliculas

#Utilizar funciones y mandar llamar desde otro archivo
#Utilizar listar para almacenar los nombres de peliculas
import os
import ListaPelis
os.system('cls')

def mostrar_menu():
    print("\n.:Gestión de Pelíclones:. ")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            nombre = input("Ingrese el nombre de la película a agregar: ")
            ListaPelis.agregar_pelicula(nombre)
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la película a remover: ")
            ListaPelis.remover_pelicula(nombre)
        
        elif opcion == '3':
            ListaPelis.consultar_peliculas()
        
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

ejecutar_programa()
