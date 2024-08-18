from ConectarBD import *
import hashlib

class Usuario:
    def __init__(self, nombre,apellido,email,password):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.contrasena = password
    
    #Funcion para encriptar la contraseña
    # def hash_password(self,contrasena):
    #     return hashlib.sha256(contrasena.encode()).hexdigest()
   
    def registrar(self):
        try:
            cursor.execute(
                "insert into usuarios values (null,%s,%s,%s,%s)",
                (self.nombre,self.apellido,self.email,self.contrasena)
            )
            conexion.commit()
            return True
        except:
            return False    

    @staticmethod
    def iniciar_sesion(email,contrasena):
        #contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        try:
           cursor.execute(
             "select * from usuarios where email=%s and password=%s",
             (email,contrasena)
           )
           usuario=cursor.fetchone()
           if usuario:
               return usuario
           else:
               return None    
        except:    
            return None  
        

