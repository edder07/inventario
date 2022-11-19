import psycopg2
from connection.bd import conexion


class CrudProducto():
    def __init__(self, data) -> None:
        self.__data = data
            
    def post_producto(self):
        categoria = self.__data["categoria"]
        nombre = self.__data["nombre"]
        sku = self.__data["sku"]
        descripcion = self.__data["descripcion"]
        precio_venta = self.__data["precio_venta"]
        estado = self.__data["estado"]
        
        try:
            with conexion.cursor() as cursor:
                consulta = "insert into producto(producto_categoria_id,nombre,sku,descripcion,precio_venta,estado) values (%s,%s,%s,%s,%s,%s);"
                cursor.execute(consulta, (categoria,nombre,sku,descripcion,precio_venta,estado,))
                conexion.commit()
            return self.__data

        except psycopg2.Error as e:
            print("Ocurrió un error al insertar: ", e)
        
    def get_producto_to_sku(self):
        sku = self.__data
        
        try:
            with conexion.cursor() as cursor:
                consulta = "select * from producto where producto.sku = %s;"
                cursor.execute(consulta, (sku,))
                mascotas = cursor.fetchall()

                # Recorrer e imprimir
                for mascota in mascotas:
                    print(list(mascota))
                
                print("data_select : ", mascotas)
                return mascotas
                            
        except psycopg2.Error as e:
            print("Ocurrió un error al seleccionar por sku: ", e)
