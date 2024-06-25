'''
2.- 
Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for
'''
import os
os.system('clear')
valores = [ ]

suma=1
while len(valores) < 120:
    valores.append(suma)
    suma += 1
    
print('La lista de numeros es: ')
for numero in valores:
   print(numero)

print('Los numeros llegan hasta el 120')