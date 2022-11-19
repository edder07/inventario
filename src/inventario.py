import psycopg2
from connection.bd import conexion


class CrudInventario():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_inventario(self):
        nombre = self.__data["nombre"]
        print(self.__data)
        
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into inventario(nombre) values (%s);"
                cursor.execute(consulta, (nombre,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
