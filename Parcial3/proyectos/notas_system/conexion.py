import mysql.connector

#Conectar con la BD en MySQL
try:
    conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bd_notas'
)
#Crear un objeto de tipo cursor que permita reutilizar el objeto
    cursor=conexion.cursor(buffered=True)
except Exception as e:
    print("Ocurrio un error con el servidor ... por favor verifique...")
    
else: 
#Verificar si la conexion fue exitosa
 if conexion.is_connected():
    print("La conexion con la BD  fue exitosa ")


