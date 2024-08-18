# ConectarBD.py
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="finalskate"
    )
    cursor = conexion.cursor()
except mysql.connector.Error as err:
    print(f"Ha ocurrido un error en la conexión a la BD: {err}")

    

