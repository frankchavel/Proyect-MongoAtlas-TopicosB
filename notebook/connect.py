from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
load_dotenv()
MONGODB_URI_ATLAS = os.getenv("MONGODB_URI_Atlas")
DATABASE_NAME = os.getenv("MongoDB_Data")

client = MongoClient(MONGODB_URI_ATLAS)
print("Conexión exitosa a MongoDB Atlas")
db = client[DATABASE_NAME]

try:
    client = MongoClient(MONGODB_URI_ATLAS)
    print("Conexión exitosa a MongoDB Atlas")
    db = client[DATABASE_NAME]

    colecciones = db.list_collection_names()
    print("Colecciones en la base de datos:", (DATABASE_NAME))
    print("Colecciones:", (colecciones))
except errors.ServerSelectionTimeoutError as e:
    print("Error de conexión a MongoDB Atlas")

except errors.OperationFailure as e:
    print("Error de Autenticación o permisos", e)