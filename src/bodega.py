import psycopg2
from connection.bd import conexion


class CrudBodega():
    def __init__(self, data) -> None:
        self.__data = data
    
    def get_all_bodega(self):
        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM bodega;")
                return_select = cursor.fetchall()
                print("data_select : ", return_select)
                return return_select
                            
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)
       
            
    def get_single_bodega(self):
        data_id = self.__data["bodega_id"]
        print(data_id)
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT * FROM bodega where bodega.bodega_id = %s;"
                cursor.execute(consulta, (data_id,))

                return_select = cursor.fetchall()
                print("data_select : ", return_select)
                return return_select
                            
        except psycopg2.Error as e:
            print("Ocurrió un error al consultar: ", e)

            
    def post_bodega(self):
        data_nombre = self.__data["nombre"]
        print(data_nombre)
       
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into bodega(nombre) values (%s);"
                cursor.execute(consulta, (data_nombre,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
            
    def delete_bodega(self):
        data_nombre = self.__data["nombre"]
        print(data_nombre)
       
        try:
            with conexion.cursor() as cursor:

                consulta = "delete from bodega where bodega.nombre= %s;"
               
                cursor.execute(consulta, (data_nombre,))

            conexion.commit()
            return self.__data
        except psycopg2.Error as e:
            print("Error eliminando: ", e)
