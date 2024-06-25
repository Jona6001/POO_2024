"""
List (Array)
son colecciones o conjuntos de datos/valores bajo 
un mismo nombre, para acceder a los valores 
se hace con un indice numerico

nota: Sus valores si son modificables

La lista es una coleccion ordenada y modificable, permite miembros duplicados

"""
import os


#Ejemplo 1 crear una lista con datos numericos e imprimir el contenido

lista=[23,24]
print(lista)

#Recorre la lista con for
for i in lista:
    print(i)

#Recorrer la lista con el While
i=0
while i<=len(lista)-1:
    print(lista[i])
    i+=1


#Ejemplo 2   Crear una lista de 4 palabras, solicitar una palabra y buscar la coincidencia 
#en la lista e indicar si la encontro o no y en que posicion.

palabras=['Hola','6001','Byee','UTD']
print(palabras)

palabra_buscar=input('Igresa la palabra a buscar: ')

noencontre=True

# for i in palabras:
#     if palabra_buscar==i:
#          print(f'Enontre la palabra {i}, en la posicion: {palabras.index(i)}')
#          noencontre=False
    
# if noencontre: 
#     print('No encontre la palabra')

p=0
while p<len(palabras):
    if palabra_buscar==palabras[p]:
     print(f'Enontre la palabra {palabra_buscar}, en la posicion: {p}')
    noencontre=False
    p+=1

if noencontre:
    print(f'No encontre la palabra')


#Ejemplo 3 Agregar y Eliminar elementos de una lista

numeros=[23,61]
print(numeros)

#Agregar un elemento
numeros.append(100)
print(numeros)

numeros.insert(3,200)
print(numeros)

#Eliminar elementos 
numeros.remove(100) #Se debe de indicar el elemento a eliminar, si hay 2 iguales se eliminan ambos
print(numeros)

numeros.pop(2) #Se debe de indicar la posicion en la lista para eliminarla
print(numeros)

os.system('cls')

#Ejemplo 4 Crear una lista multidimensional (MATRIZ) para almacenar los contactos te;efonicos
Agenda=[
   'Carlos',618232332,
   'Karin',618943058,
   'Leon',618983940,
   'Pedro',6181574381,
   ]
print(Agenda)
for i in Agenda:
   print(f'{Agenda.index(i) +1}.- {i} ')




