#Solicitar 2 numeros al usuario
# y realizar todas las operaciones
# basicas de una calculadora (+,-,*,/)
# y mostrar por pantalla el resultado


num1=float (input("Ingresa el primer numero: "))
num2=float (input("Ingresa el segundo numero: "))

suma= num1 + num2
resta= num1 - num2
multi= num1*num2
divi= num1/num2

print(f"Las operaciones son las siguientes: ")
print(f"La suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La multiplicacion es: {multi}")
print(f"La division es: {divi}")