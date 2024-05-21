# Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

numInicial = int(input("Introduce el primer número: "))
numFinal = int(input("Introduce el segundo número: "))

if numInicial > numFinal:
    numInicial, numFinal = numFinal, numInicial

print(f"Los números entre {numInicial} y {numFinal} son: ")
for num in range(numInicial + 1, numFinal):
    print(num)
