import psycopg2
import os

def is_db_connected():
    try:
        conn = psycopg2.connect(os.getenv('DATABASE_URL'), sslmode='require')
        conn.close()
        return True
    except Exception:
        return False
