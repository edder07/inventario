import psycopg2
from connection.bd import conexion


class CrudCategoria():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_categoria(self):
        nombre = self.__data["nombre"]
        inventario = self.__data["inventario"]
        
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into categoria(nombre,categoria_inventario_id) values (%s,%s);"
                cursor.execute(consulta, (nombre,inventario,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
