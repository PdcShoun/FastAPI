from contextlib import asynccontextmanager

from app.database.engine import create_db_and_tables


@asynccontextmanager
async def lifespan(app):
    create_db_and_tables()
    yield
