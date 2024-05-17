#El ciclo WHILE es una estructura de coontrol que itera o repite la ejecucion 
#de una serie de instrucciones tantas veces como la condicion se cumpla
# "TRUE" 

# Sintaxis:
#  while condicion:
#  bloque de instrucciones

#Ejemplo 1: Crear un programa que imprima 5 veces el caracter "@"
contador=1
while contador<=5:
    print("@")
    contador+=1

#Ejemplo 2: Crear un programa que imprima los numeros del 1 al 6, los sume y al final imprima la suma
Contador=1
suma=0
while Contador<=5:
    print(f"{Contador}")
    suma+=Contador
    Contador+=1
    print(f"la suma es {suma}")

    #Ejemplo 3: Crear un programa que solicite un numero entero y a continuacion imprima 
#la tabla de multiplicar correspondiente,

numeroo=int(input("Ingresa un numero: "))
num=1
multi=0
i=1
while i<=10:
 multi=i*num
print(f"{num} X {i} = {multi}")
i+=1