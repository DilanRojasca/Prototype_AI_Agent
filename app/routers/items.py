#crud 1)create 2)read 3)update 4)delete
from fastapi import APIRouter, Depends, HTTPException, status
import json
import os
from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException, status
from app.db.json_db import read_database, write_database
from app.schemas.item import ItemCreate


router = APIRouter()



@router.get("/items/{item_id}")
def get_item(item_id: int):
    data = read_database()
    for item in data:
        if item["ID"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@router.post("/items/")
def add_item(item: ItemCreate):
    data = read_database()
    data.append(item.dict())
    write_database(data)
    return {"message": "Item agregado"}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    data = read_database()
    new_data = [item for item in data if item["ID"] != item_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Item no encontrado")
    write_database(new_data)
    return {"message": "Item eliminado"}




def create_new_item():
    ID = input("Ingrese el ID del item: ")
    NombreCliente = input("Ingrese el Nombre del Cliente: ")                        
    Sector = input("Ingrese el Sector: ")
    ProductoEmpacar = input("Ingrese el Producto a Empacar: ")                      
    Formato = input("Ingrese el Formato: ")
    Presentacion = input("Ingrese la Presentacion: ")   
    VidaUtil = input("Ingrese la Vida Util: ")
    Anaquel = input("Ingrese el Anaquel: ") 
    Conservacion = input("Ingrese la Conservacion: ")   
    ProcesosTermicos = input("Ingrese los Procesos Termicos (separados por comas): ").split(",")
    TemperaturaProceso = input("Ingrese la Temperatura del Proceso: ")                                
    EstructuraActual = input("Ingrese la Estructura Actual: ")
    RequiereAditamentos = input("¿Requiere Aditamentos? (si/no): ")
    Aditamento = input("Ingrese el Aditamento: ") if RequiereAditamentos.lower() == "si" else "No Aplica"
    Dimensiones = {                         
        "Largo": input("Ingrese el Largo: "),
        "Ancho": input("Ingrese el Ancho: "),
        "Alto": input("Ingrese el Alto: ")
    }      
    return {
        "ID" : ID,
        "NombreCliente" : NombreCliente,
        "Sector" : Sector,
        "ProductoEmpacar" : ProductoEmpacar,
        "Formato" : Formato,
        "Presentacion" : Presentacion,
        "VidaUtil" : VidaUtil,
        "Anaquel" : Anaquel,
        "Conservacion" : Conservacion,
        "ProcesosTermicos" : ProcesosTermicos,
        "TemperaturaProceso" : TemperaturaProceso,
        "EstructuraActual" : EstructuraActual,
        "RequiereAditamentos" : RequiereAditamentos,
        "Aditamento" : Aditamento,
        "Dimensiones" : Dimensiones,
    }                                                                      

    create_new_item;
    
    