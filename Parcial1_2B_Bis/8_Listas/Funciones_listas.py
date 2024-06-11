import os

paises=['Mexico','USA','Brasil','Japon']
numero=[23,34,12.56,0.100,23]
texto=['Hola',True,23,3.141516]

#Ordenar una lista

print(paises)
paises.sort() 
print(paises)

print(numero)
numero.sort()
print(numero)

print(texto)

print(texto)

#Agrar elementos
print(texto)
texto.insert(len(texto),'True') #Inserta un elemento en un indice especifico
print(texto)
texto.insert(len(texto),True)
print(texto)

texto.append(False) #Insertar un elemento al final de la lista
print(texto)

#Eliminar elementos
print(numero)
numero.remove(23)
print(numero)
numero.pop(0)
print(numero)

os.system('cls')

#Dar la vuelta a una lista
print(numero)
numero.reverse()
print(numero)

#Buscar un dato dentro de una lista
respuesta='Brasil' in paises
print(respuesta) 

#Cuantas veces aparece un valor dentro de una lista
print(numero)
numero.append(23)
cuantos=numero.count(23)
print(f'El numero 23 se encontro: {cuantos} veces')


#Unir listas
print(paises)
paises.extend(numero)
print(paises)



