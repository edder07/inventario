import logging
from fastapi import FastAPI

from src.bodega import CrudBodega
from src.usuario import CrudUsuario
from src.local_venta import CrudLocal
from src.producto import CrudProducto
from src.categoria import CrudCategoria
from src.movimiento import CrudMovimiento
from src.inventario import CrudInventario


from fastapi import HTTPException
from src.exceptions import JoinJsonError



logging.getLogger().setLevel(logging.INFO)
api = FastAPI()

############    BODEGA      ###############################################################################
@api.post("/v1/get_all_bodega")
def get_all_bodega(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudBodega(data)
        data_converted = json_data.get_all_bodega()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in GET ALL Bodega: {ex}")
        raise HTTPException(
            400,
            "Error in GET ALL Bodega"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted

@api.post("/v1/get_single_bodega")
def get_single_bodega(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudBodega(data)
        data_converted = json_data.get_single_bodega()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in GET SINGLE Bodega: {ex}")
        raise HTTPException(
            400,
            "Error in GET SINGLE Bodega"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


@api.post("/v1/post_bodega")
def post_bodega(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudBodega(data)
        data_converted = json_data.post_bodega()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST Bodega: {ex}")
        raise HTTPException(
            400,
            "Error in POST Bodega"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


@api.delete("/v1/delete_bodega")
def delete_bodega(data: dict):
    logging.info(f"Arrived Data to DELETE: {data}")
    try:
        json_data = CrudBodega(data)
        data_response = json_data.delete_bodega()
        print(data_response)
    except JoinJsonError as ex:
        logging.error(f"Error on data DELETE: {ex}")
        raise HTTPException(
            400,
            "Error in DELETE data"
        )

    logging.info(
        f"Data response to DELETE BODEGA: {data_response}")

    return data_response

##############    USUARIO    ################################################################################

@api.post("/v1/post_usuario")
def post_usuario(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudUsuario(data)
        data_converted = json_data.post_usuario()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST Usuario: {ex}")
        raise HTTPException(
            400,
            "Error in POST Usuario"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


#######################        PRODUCTO      ###########################################################

@api.post("/v1/post_producto")
def post_producto(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudProducto(data)
        data_converted = json_data.post_producto()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST Producto: {ex}")
        raise HTTPException(
            400,
            "Error in POST Producto"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


@api.get("/v1/get_producto/sku/{sku}")
def get_producto(workflow_id: str):
    logging.info(f"order arrived Data: {workflow_id}")
    try:
        json_data = CrudProducto(workflow_id)
        data_converted = json_data.get_producto_to_sku()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST Producto: {ex}")
        raise HTTPException(
            400,
            "Error in GET Producto por sku"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


#######################      CATEGORIA       #################################################################


@api.post("/v1/post_categoria")
def post_categoria(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudCategoria(data)
        data_converted = json_data.post_categoria()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST CATEGORIA: {ex}")
        raise HTTPException(
            400,
            "Error in POST CATEGORIA"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted

#####################      INVENTARIO      ################################################################
@api.post("/v1/post_inventario")
def post_inventario(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudInventario(data)
        data_converted = json_data.post_inventario()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST INVENTARIO: {ex}")
        raise HTTPException(
            400,
            "Error in POST INVENTARIO"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


#####################      LOCAL DE VENTA      ################################################################
@api.post("/v1/post_local")
def post_local(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudLocal(data)
        data_converted = json_data.post_local()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST INVENTARIO: {ex}")
        raise HTTPException(
            400,
            "Error in POST INVENTARIO"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted


#####################     MOVIMIENTO     ################################################################
@api.post("/v1/post_movimiento")
def post_movimiento(data: dict):
    logging.info(f"order arrived Data: {data}")
    try:
        json_data = CrudMovimiento(data)
        data_converted = json_data.post_movimiento()
        print(data_converted)
    except JoinJsonError as ex:
        logging.error(f"Error in POST MOVIMIENTO: {ex}")
        raise HTTPException(
            400,
            "Error in POST MOVIMIENTO"
        )

    logging.info(
        f"Data transformed: {data_converted}")

    return data_converted
