from fastapi import FastAPI
"""Точки входа для API"""

from src.db import SessionLocal #для создания нового подключения к базе
from sqlalchemy import text #оборачиваем команду в текст для SQLALchemy 
from fastapi import Depends #импортируем зависимости
from sqlalchemy.ext.asyncio import AsyncSession
print("LOADED MY MAIN.PY")
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

#FastAPI  →  SQLAlchemy AsyncSession → asyncpg → PostgreSQL

@app.get("/test")
async def test_db(
    session: AsyncSession = Depends(get_session)
):
    result = await session.execute(text("SELECT 1"))

    return {
        "status": "success",
        "db_response": result.scalar()
    }
