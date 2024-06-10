x=20

def ciudadPeluche():
    print(x)

def springfield():
    global x
    x=6 

ciudadPeluche()
springfield()
print('El cambio es: ',x)