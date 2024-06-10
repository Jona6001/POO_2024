# Hacer un programa que solicite numeros 
#indefinidamente hasta que se introduzca el 111 y salir del programa

while True:
    numero = int(input("Introduce un número (usa 111 para salir): "))
    if numero == 111:
        print("¡Introdujiste 111! Saliendo del programa.")
        break
    else:
        print(f"Has introducido el número: {numero}")
