from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class ItemBase(BaseModel):
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

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    ID: int
