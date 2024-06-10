"""
Esiste una estructura de condicion llamada "if"
La cual evalua la condicion para encontrar el valor "True" o se cumple 
la condicion se ejecuta la linea o lineas de codigo


Tienes 3 variantes de if
1.-if simple
2.-if compuesto
3.-if anidado
4.-if elif
"""
#Ejemplo 1.- if simple 
color="rojo"
if color=="rojo":
    print("Soy el color rojo")


#Ejemplo 2.- if compuesto 
color="rojo"
if color=="rojo":
    print("Soy el color rojo")
else: print("No soy el color rojo")

#Ejemplo 3.- if anidado
color="rojo"
if color=="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("Soy el rojo")
else:
    print("No soy el color rojo")
    if color!="rojo":
        print("Soy otro color")

#Ejemplo 4.- if con elif
color="rojo"
if color=="rojo":
    print("Soy el color rojo")
elif color=="negro":
    print("Soy el negro")
elif color=="verde":
    print("Soy el verde")
else:
    print("No soy rojo, negro o verde")
