import mysql.connector

#Conectar con la BD en MySQL
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_pythonn'
)
except Exception as e:
    print(f"Error: {type (e)}")
    print(f"Tipo de error: {type (e).__name__}")
    print("Ocurrio un error con el servidor ... por favor verifique...")
    
else: 
#Verificar si la conexion fue exitosa
 if conexion.is_connected():
    print("La conexion con la BD  fue exitosa ")
