from ConectarBD import *

class Ropa():
    def __init__(self, nombre, precio, cantidad, talla, material, stock_max, stock_min):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.talla = talla
        self.material = material
        self.stock_max = stock_max
        self.stock_min = stock_min

    def agregar(self):
        try:
            cursor.execute(
                "INSERT INTO ropa (nombre, precio, cantidad, talla, material, stock_max, stock_min) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (self.nombre, self.precio, self.cantidad, self.talla, self.material, self.stock_max, self.stock_min)
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
                "UPDATE ropa SET cantidad = 0 WHERE id = %s",
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
                "DELETE FROM ropa WHERE id = %s",
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
                "UPDATE ropa SET cantidad = %s WHERE id = %s",
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
            cursor.execute("SELECT * FROM ropa")
            return cursor.fetchall()
        except Exception as e:
            print(e)
            return False

         
    
      