import databases
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from .configs import settings


class Database:
    DB_URL = f'postgresql+asyncpg://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DATABASE}'

    engine = create_async_engine(DB_URL)

    session = sessionmaker(
        bind=engine, autocommit=False, expire_on_commit=False, class_=AsyncSession
    )


settings_db = Database()
database = databases.Database(settings_db.DB_URL)
