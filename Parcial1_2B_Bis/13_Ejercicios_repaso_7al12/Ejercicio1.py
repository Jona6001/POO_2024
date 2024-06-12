'''
1.- 

 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado
'''
import os
os.system('clear')

numeros=[6,4,2,4,1,7,9,8]

# a.- Recorrer la lista y mostrarla
print("Lista original:")
for numero in numeros:
    print(numero)


# b.- Hacer una función que recorra la lista de números y devuelva un string
def listaString(lista):
   return ' '.join(map(str, lista))
string_lista = listaString(numeros)
print("Lista como string:", string_lista)


# c.- Ordenarla y mostrarla
numeros_ordenados = sorted(numeros)
print("Lista ordenada:", numeros_ordenados)


# d.- Mostrar su longitud
print("La longitud de la lista es de:", len(numeros))


# e.- Buscar algún elemento que el usuario pida por teclado
try:
 buscar_numero = int(input("Introduce el numero que quieres buscar: "))
 if buscar_numero in numeros:
    print(f"El numero {buscar_numero} si se encuentra en la lista.")
 else:
    print(f"El numero {buscar_numero} no se encuentra en la lista.")

except ValueError:
   print('Es necesario que se ingrese un numero del teclado, las letras no son aceptadas')
   print('Ejecuta el programa de nuevo.')