import os
import json

# Ruta absoluta al archivo Database.JSON (ajusta si tu estructura cambia)
DATABASE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "Database.JSON")
DATABASE_PATH = os.path.abspath(DATABASE_PATH)

def read_database():
    with open(DATABASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def write_database(data):
    with open(DATABASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)