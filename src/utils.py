import psycopg2
from connection.bd import conexion


class Crud():
    def __init__(self, data) -> None:
        self.__data = data
    
    def get_all_items(self):
        try:
            with conexion.cursor() as cursor:
                # En este caso no necesitamos limpiar ningún dato
                cursor.execute("SELECT * FROM bodega;")
                # Hacer un while, mientras fetchone no regrese None
                data_select = cursor.fetchone()
                while data_select:
                    print("salida 1: ", data_select)
                    return data_select
                    
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
        finally:
            conexion.close()
