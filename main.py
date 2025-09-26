from fastapi import FastAPI
from app.routers import items
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("API iniciada correctamente.")
    yield
    print("API finalizada.")

app = FastAPI(
    title="Prototype AI Agent API",
    description="API para gestión de items con FastAPI y almacenamiento en JSON.",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(items.router, prefix="/api", tags=["Items"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API Prototype AI Agent"}