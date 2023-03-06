from .database import Database

database = Database()


def get_session():
    session = database.session()
    try:
        yield session
    finally:
        session.close()
