from ConectarBD import *

class Accesorios():
    def __init__(self, nombre, precio, cantidad, tipo, stock_max, stock_min):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.tipo = tipo
        self.stock_max = stock_max
        self.stock_min = stock_min

    def agregar(self):
        try:
            cursor.execute(
                "INSERT INTO accesorios (nombre, precio, cantidad, tipo, stock_max, stock_min) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.nombre, self.precio, self.cantidad, self.tipo, self.stock_max, self.stock_min)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def eliminarStock(id):
        try:
            cursor.execute(
                "UPDATE accesorios SET cantidad = 0 WHERE id = %s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False 

    @staticmethod
    def eliminarProducto(id):
        try:
            cursor.execute(
                "DELETE FROM accesorios WHERE id = %s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def actualizarCantidad(id, cantidad):
        try:
            cursor.execute(
                "UPDATE accesorios SET cantidad = %s WHERE id = %s",
                (cantidad, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def mostrarProducto():
        try:
            cursor.execute("SELECT * FROM accesorios")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False

         
    
      