class Figuras():
    def calcular_Area(self):
        pass

#Rectangulo
class Rectangulo(Figuras):

    def __init__(self, largo, ancho):
        self.largo=largo
        self.ancho=ancho

    def getLargo(self):
        return self.largo
    def setLargo(self, valor):
        self.largo = valor


    def getAncho(self):
        return self.ancho
    def setAncho(self, valor):
        self.ancho = valor

    def calcular_area(self):
        return self.largo * self.ancho
    
    
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y
    def setX(self, y):
        self.y = y
    
    def getVisible(self):
        return self.visible
    def setVisible(self,visible):
        self.visible=visible

    def getInfo(self):
        print(f"El valor de X es: {self.getX()} y el valor de Y es: {self.getY()} \n 
              Es visible : {self.getVisible} \n 
              El alto es: {self.getLargo} y su anchura es de: {self.getAncho} \n 
              El area es: {self.calcular_Area}")


#Circulo
class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def getRadio(self):
        return self.radio
    def setRadio(self, valor):
        self.radio = valor

    def calcular_area(self):
        import math
        return math.pi * (self.radio ** 2)
    
    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y
    def setX(self, y):
        self.y = y

    def getVisible(self):
        return self.visible
    def setVisible(self,visible):
        self.visible=visible
    
    def getInfo(self):
        print(f"El valor de X es: {self.getX()} y el valor de Y es: {self.getY()} \n 
              Es visible : {self.getVisible} \n 
              El radio es de : {self.getRadio}")