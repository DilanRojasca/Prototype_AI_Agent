# Semillero_SYSLAC API

Este proyecto es una API construida con FastAPI que utiliza un archivo JSON (`Database.JSON`) como base de datos para almacenar y gestionar información de clientes y productos.

## Características
- API REST con FastAPI
- Lectura, creación y eliminación de registros en `Database.JSON`
- Estructura de datos basada en Pydantic

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Instala las dependencias:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Uso
1. Asegúrate de tener el archivo `Database.JSON` en la raíz del proyecto.
2. Ejecuta el servidor con:
   ```bash
   .venv/bin/uvicorn main:app --reload
   ```
3. Accede a la documentación interactiva en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints principales
- `GET /` — Lista todos los registros
- `GET /items/{item_id}` — Obtiene un registro por ID
- `POST /items/` — Agrega un nuevo registro
- `DELETE /items/{item_id}` — Elimina un registro por ID

## Estructura de un registro
```json
{
  "ID": 1,
  "NombreCliente": "Cliente_1",
  "Sector": "Cuidado personal",
  "ProductoEmpacar": "Detergente líquido",
  "Formato": "Doypack",
  "Presentacion": "500 ml",
  "VidaUtil": "6 meses",
  "Anaquel": "3 meses",
  "Conservacion": "Congelación",
  "ProcesosTermicos": ["Empacado en caliente"],
  "TemperaturaProceso": "75ºC",
  "EstructuraActual": "PET//HBA",
  "RequiereAditamentos": "No",
  "Aditamento": "Boquilla",
  "Dimensiones": {"alto": "18 cms", "ancho": "12 cms", "fuelle": "5 cms"},
  "RequiereEstructuraSostenible": "No",
  "RequiereImpresion": "Si",
  "OpcionesEstructurasRecomendar": ["PET//HBA", "PET//FLEXIBLE", "PET//PET METALIZADO//PEBD"],
  "EstructuraRecomendada": "PET//HBA"
}
```

## Licencia
Este proyecto es de uso académico y libre.
