#Es un ciclo iterativo que se ejecuta x veces de acuerdo al rango de acuerdo a los valores numericos enteros establecidos.

# sitaxis:
# for variable in elemento_iterable (Lista, rango, etc.)
#              Bloque deinteracciones

#Ejemplo 1: Crear un programa que imprima 5 veces el caracter "@"
contador=1
for contador in range (1,6):
 print("@")


#Ejemplo 2: Crear un programa que imprima los numeros del 1 al 6, los sume y al final imprima la suma
suma=0
for numero in range (1,6):
 suma+=numero
print(f"la suma es: {suma}")

#Ejemplo 3: Crear un programa que solicite un numero entero y a continuacion imprima 
#la tabla de multiplicar correspondiente,

numeroo=int(input("Ingresa un numero: "))
multi=0
for i in range (1,11):
 multi=i*numeroo
 print(f"{numeroo} X {i} = {multi}")
