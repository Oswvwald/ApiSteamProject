from psycopg2 import pool
import os
from dotenv import load_dotenv
import urllib.parse as urlparse

load_dotenv()

# Analizar la URL de conexión
url = urlparse.urlparse(os.getenv("DATABASE_URL"))

# Extraer parámetros
db_config = {
    "dbname": url.path[1:],
    "user": url.username,
    "password": url.password,
    "host": url.hostname,
    "port": url.port
}

# Crear pool de conexiones
conecction_pool = pool.ThreadedConnectionPool(
    minconn=1,
    maxconn=10,
    **db_config
)

def get_connection():
    return conecction_pool.getconn()

def put_connection(conn):
    conecction_pool.putconn(conn)

def close_all_connections():
    conecction_pool.closeall()
