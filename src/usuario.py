import psycopg2
from connection.bd import conexion


class CrudUsuario():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_usuario(self):
        nombre = self.__data["nombre"]
        apellido = self.__data["apellido"]
        estado = self.__data["estado"]
        usuario = self.__data["usuario"]
        password = self.__data["password"]
        print(self.__data)
        
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into usuario(nombre,apellido,estado,usuario,password) values (%s,%s,%s,%s,%s);"
                cursor.execute(consulta, (nombre,apellido,estado,usuario,password,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
