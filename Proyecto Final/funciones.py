# funciones.py
from ConectarBD import *


def LimpiarPantalla():
    import os
    os.system("cls")

def EsperaTecla():
    print(f"\t \t ..::   Oprima cualquier tecla para continuar...   ::..")
    input()