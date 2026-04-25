import psycopg2
from config import params

def connect():
    try:
        return psycopg2.connect(**params)
    except Exception as error:
        print(f"Connection Error: {error}")
        raise 