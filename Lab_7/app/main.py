from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import os
import time

app = FastAPI(title="News Aggregator API")

# Настройки БД (берутся из переменных окружения Docker Compose)
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "newsdb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "password")

class NewsItem(BaseModel):
    title: str
    content: str

def get_db_connection():
    # Ждем, пока база данных поднимется (полезно при старте контейнеров)
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Could not connect to the database")

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Инициализируем БД при старте приложения
@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/news")
def add_news(item: NewsItem):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "INSERT INTO news (title, content) VALUES (%s, %s) RETURNING id, title, content, created_at",
        (item.title, item.content)
    )
    new_news = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return new_news

@app.get("/news")
def get_news(limit: int = Query(10, ge=1), offset: int = Query(0, ge=0)):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, title, content, created_at FROM news ORDER BY created_at DESC LIMIT %s OFFSET %s",
        (limit, offset)
    )
    news_list = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"total_returned": len(news_list), "limit": limit, "offset": offset, "news": news_list}
