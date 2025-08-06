import os
from sqlalchemy import create_engine

DB_URL = os.getenv('DB_URL')  # Fetch from environment variable

def get_db_connection():
    try:
        engine = create_engine(DB_URL)
        return engine
    except Exception as e:
        print(f"Error: {e}")
        raise
