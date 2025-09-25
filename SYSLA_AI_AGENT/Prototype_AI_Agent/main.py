
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "Database.JSON")

def read_database():
    with open(DATABASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_database(data):
    with open(DATABASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.get("/")
def get_all_items():
    return read_database()

class Item(BaseModel):
    ID: int
    NombreCliente: str
    Sector: str
    ProductoEmpacar: str
    Formato: str
    Presentacion: str
    VidaUtil: str
    Anaquel: str
    Conservacion: str
    ProcesosTermicos: list
    TemperaturaProceso: str
    EstructuraActual: str
    RequiereAditamentos: str
    Aditamento: str
    Dimensiones: dict
    RequiereEstructuraSostenible: str
    RequiereImpresion: str
    OpcionesEstructurasRecomendar: list
    EstructuraRecomendada: str
	
@app.get("/items/{item_id}")
def get_item(item_id: int):
    data = read_database()
    for item in data:
        if item["ID"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")

@app.post("/items/")
def add_item(item: Item):
    data = read_database()
    data.append(item.dict())
    write_database(data)
    return {"message": "Item agregado"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    data = read_database()
    new_data = [item for item in data if item["ID"] != item_id]
    if len(new_data) == len(data):
        raise HTTPException(status_code=404, detail="Item no encontrado")
    write_database(new_data)
    return {"message": "Item eliminado"}
    