"""
Comentario de varias lineas
nota: cuando se imprime en pantalla una cadena de caracteres se trabaja por default con "cadenas", es decir
 Python no puede concatenat otra cosa que no sea un string (str)
"""


#Comentario de una linea

texto="Soy una cadena dee caracteres"
numero=23

#conectar str con str
print("Soy otra cadena Y", texto, )

#Concatenar str con int
print("El número es: ","\"numero""\"", "Esta es la forma de agregarle comillas a una variable")

#Conectar con int con str

n1=int('23')
n2=33
suma=n1+n2
#Primera forma
print("La suma es: "+str(suma))
#3ra FORMA 
print(f"La suma es: {suma}")


#Conectar float y int con str

n3=23.99
n4=33.0
sumar=float(n3)+n4
sumaar=int(n3+n4)
#3ra FORMA de concatenar 
print(f"La suma con float es: {sumar}")
print(f"La suma truncada es: {sumaar}")