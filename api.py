import logging
from fastapi import FastAPI
from src.bodega import CrudBodega
from fastapi import HTTPException
from src.exceptions import JoinJsonError



logging.getLogger().setLevel(logging.INFO)
api = FastAPI()


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
