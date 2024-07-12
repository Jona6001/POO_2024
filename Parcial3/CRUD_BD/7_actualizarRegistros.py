from conexionBD import *
try:

    micursor=conexion.cursor()
    sql="update clientes set direccion='Col. Nueva Vizcaya' WHERE id=1 "

    micursor.execute(sql)
    conexion.commit()
except:
    print("Ha ocurrido un error!! ...VERIFICA..")
else:
 print("Registro(s) Actualozado(s) exitosamente!!")