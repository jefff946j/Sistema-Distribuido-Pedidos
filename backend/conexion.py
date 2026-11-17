
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_conexion():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="gestion_pedidos",
        port=3306
    )
    return conexion
