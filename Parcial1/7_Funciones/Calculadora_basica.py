import os

def solicitarDatos():
    n1 = int(input('Número #1: '))
    n2 = int(input('Número #2: '))
    return n1, n2

def getCalculadora(n1, n2, operacion):
    if operacion == '+' or operacion.lower()=='suma':
        return f'{n1} + {n2} = {n1 + n2}'
    elif operacion == '-' or operacion.lower()=='resta':
        return f'{n1} - {n2} = {n1 - n2}'
    elif operacion == '*' or operacion.lower()=='multiplicar':
        return f'{n1} * {n2} = {n1 * n2}'
    elif operacion == '/' or operacion.lower()=='division':
        if n2 != 0:
            return f'{n1} / {n2} = {n1 / n2} '
        else:
            return 'Es imposible dividir entre 0'
    else:
        return 'Operación no válida'

def esperaTecla():
    print('Presiona cualquier tecla para continuar...')

    input()

while True:
    os.system('clear')
    print('\n   ..: CALCULADORA :.. ')
    operacion = input("Ingresa el tipo de operación que vas a realizar usando signos o el nombre de los mismos (+, -, *, /) \n usa 'salir' para terminar: ")
    if operacion.lower() == 'salir':
        print("Saliendo de la calculadora.")
        break
    n1, n2 = solicitarDatos()
    resultado = getCalculadora(n1, n2, operacion)
    print(resultado)
    esperaTecla()
