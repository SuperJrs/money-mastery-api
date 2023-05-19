import databases
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .configs import settings


class Database:
    DB_URL_ASYNC = f'postgresql+asyncpg://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DATABASE}'
    DB_URL_SYNC = f'postgresql://{settings.USER}:{settings.PASSWORD}@{settings.HOST}/{settings.DATABASE}'

    engine = create_async_engine(DB_URL_ASYNC)

    Session = sessionmaker(
        bind=engine,
        autocommit=False,
        expire_on_commit=False,
        class_=AsyncSession,
    )
    
    Base = declarative_base()
    


settings_db = Database()
database = databases.Database(settings_db.DB_URL_ASYNC)
