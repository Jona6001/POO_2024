'''
3.- 

Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas

'''
import os
os.system('clear')

lista=[]

if not lista:
    print('No hay nada en la lista, es necesario agregar algo.')

while True:
    entrada=input(f'Ingresa algun dato en la lista. Ingresa "Salir" para terminar con el programa. ')
    if entrada.lower()=='salir':
        break

    lista.append(entrada)

print(f'El contenido de la lista es: {lista}')

print(f'El contenido de la lista en mayusculas es: ')
for mayus in lista:
 print(mayus.upper())