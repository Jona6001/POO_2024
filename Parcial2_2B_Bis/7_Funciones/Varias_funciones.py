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