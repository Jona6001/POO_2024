from conexionBD import *

try:
    micursor=conexion.cursor()
    sql='CREATE TABLE clientes2 (id int PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR (60), direccion VARCHAR (120), tel VARCHAR(10))'

    micursor.execute(sql)
except:
   print(f"Ocurrio un problema!! ...Por favor verifique... ")
else:
   print(f"Se creo la tabla correctamente")
