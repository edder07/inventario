import psycopg2
from connection.bd import conexion


class CrudLocal():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_local(self):
        nombre = self.__data["local_venta_nombre"]
       
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into local_venta(local_venta_nombre) values (%s);"
                cursor.execute(consulta, (nombre,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
            
