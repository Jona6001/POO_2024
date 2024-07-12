from conexionBD import *
try:

    micursor=conexion.cursor()
    sql="delete from clientes WHERE id=2"

    micursor.execute(sql)
    conexion.commit()
except:
    print("Ha ocurrido un error!! ...VERIFICA..")
else:
 print("Registro(s) Eliminado(s) exitosamente!!")