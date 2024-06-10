#Mostrar todas las todas las tablas de multiplicar del 1 al 10
#Mostrando el resultado de la tabla y luego las multiplicaciones del 1 al 10

def imprimir_tabla(n):
    print(f"Tabla de multiplicar del {n}")
    for i in range(1, 11):
        resultado = n * i
        print(f"{n} x {i} = {resultado}")
    print()

for numero in range(1, 11):
    imprimir_tabla(numero) 

