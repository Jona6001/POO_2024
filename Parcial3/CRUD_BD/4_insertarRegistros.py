from conexionBD import conexion
try:
    micursor=conexion.cursor()
    nombre=input("Escribe tu nombre :")
    direccion=input("Escribe tu direccion: ")
    tel=input("Ingresa tu numero de telefono: ")

   # sql="INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, 'Mundo', 'Cerca de la 89', '6182944332');"
    sql=sql="INSERT INTO `clientes` (`id`, `nombre`, `direccion`, `tel`) VALUES (NULL, %s, %s, %s);"
    valores=(nombre,direccion,tel)

    micursor.execute(sql,valores)

    #El 'comit' sirve para finalizar la conexion de sql cuando se intenta hacer un insert, un update y un delete en una tabla
    conexion.commit()
except:
    print("Hubo un error verifica!")
else:
 print(f"Registro(s) insertado(s) exitosamente!!! ")