from coches import *
from coches import Camiones
from coches import Camionetas

#Crear un objetos o instanciar la clase

print("Objeto 1")
coche1=Coches("Blanco","VW","2020",220,150,5)
coche1.getInfo()


print("Objeto 2")
coche2=Coches("Azul","NISSAN","2020",180,150,5)
coche2.getInfo()

print("Objeto 3")
camion1=Camiones("negro","DINA","2020",180,200,12,8,2500)
camion1.getInfo()

print("objeto 4")
camion2=Camiones("Blanco","Star","2010",150,300,14,6,2000)
camion1.getInfo()

print("Objeto 5")
camioneta1=Camionetas("Amarilla","Renault","2025",240,250,8,"Delantera",True)
camioneta1.getInfo()

print("objeto 6")
camioneta2=Camionetas("Blanca","Nissan","2020",180,150,6,"Trasera",False)
camioneta2.getInfo()

