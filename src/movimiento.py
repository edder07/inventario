import psycopg2
from connection.bd import conexion
from datetime import datetime, date
import time


class CrudMovimiento():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_movimiento(self):
        usuario = self.__data["usuario"]
        producto = self.__data["producto"]
        local = self.__data["local"]
        tipo = self.__data["tipo"]
        cantidad = self.__data["cantidad"]
        fecha = date.today()
        hora = time.strftime("%H:%M:%S")

        print(self.__data)
        
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into movimiento(movimiento_producto_id,movimiento_usuario_id,movimiento_local_id,fecha,hora,cantidad,tipo) values (%s,%s,%s,%s,%s,%s,%s);"
                cursor.execute(consulta, (producto,usuario,local,fecha,hora,cantidad,tipo,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
