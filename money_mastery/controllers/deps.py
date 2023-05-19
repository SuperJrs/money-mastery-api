from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy import select

from ..auth.jwt_handler import JWTHandler
from ..auth.service import AuthService
from ..core.configs import settings
from ..core.database import Database, database
from ..models.conta_model import Conta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/v1/user/login')
db = Database()


def get_jwt_handler() -> JWTHandler:
    return JWTHandler(settings.KEY_JWT)


def get_auth_service() -> AuthService:
    return AuthService()


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    jwt_handler: JWTHandler = Depends(get_jwt_handler),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt_handler.decode_token(token)
        email_conta = payload.get('sub')
        if email_conta is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception
    conta = await database.fetch_one(
        select(Conta).where(Conta.email == email_conta)
    )
    if conta is None:
        raise credentials_exception
    return conta


async def get_session():
    session = db.Session()
    try:
        yield session
    finally:
        await session.close()   # type: ignore
