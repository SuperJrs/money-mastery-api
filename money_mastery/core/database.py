import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .configs import settings


class Database:
    DB_URL = f'postgresql+asyncpg://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DATABASE}'

    engine = create_engine(DB_URL)

    session = sessionmaker(
        bind=engine, autocommit=False, expire_on_commit=False
    )


settings_db = Database()
database = databases.Database(settings_db.DB_URL)
