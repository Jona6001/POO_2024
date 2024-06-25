# Hacer un programa que muestre todos los numeros impares 
# entre 2 numeros que decida el usuario
# Función para encontrar y mostrar los números impares entre dos números dados

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

def mostrar_impares(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    print(f"Números impares entre {num1} y {num2}:")
    for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num, end=" ")

mostrar_impares(num1, num2)
