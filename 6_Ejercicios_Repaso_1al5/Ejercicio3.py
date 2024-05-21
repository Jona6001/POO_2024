 # Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for


#while para recorrer los números del 1 al 60
num= 1
while num <= 60:
    cuadrado = num * num
    print(f"El cuadrado de {num} es {cuadrado}")
    num += 1

print('\n')

#For para recorrer los números del 1 al 60
for num in range(1, 61):
    cuadrado = num * num
    print(f"El cuadrado de {num} es {cuadrado}")
