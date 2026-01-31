from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()


def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host="db"
    )


@app.get("/")
def root():
    return {"status": "Backend is working"}


@app.get("/db")
def test_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT 1;")
    result = cur.fetchone()

    cur.close()
    conn.close()

    return {"db_test": result[0]}

