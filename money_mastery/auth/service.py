from typing import Optional
from fastapi import Depends

from .jwt_handler import JWTHandler
from ..models.conta_model import Conta 
from ..core.database import database
from ..schemas.conta_schema import ContaSchema
# from databases import Database
from ..repository.conta_repo import ContaRepo 
from .crypt import check_password
from ..core.configs import settings



def get_conta_repo() -> ContaRepo:
    return ContaRepo(database)

def get_jwt_handler() -> JWTHandler:
    return JWTHandler(settings.KEY_JWT)


class AuthService:
    def __init__(
        self, 
        conta_repository: ContaRepo = ContaRepo(database), 
        jwt_handler: JWTHandler = JWTHandler(settings.KEY_JWT)
    ):
        self.conta_repository = conta_repository
        self.jwt_handler = jwt_handler

    async def authenticate_user(self, email: str, password: str) -> Optional[Conta]:
        conta = await self.conta_repository.get_by_email(email)

        if conta and check_password(password, conta.senha): # type: ignore
            return conta # type: ignore

        return None

    def create_access_token(self, email: str) -> str:
        access_token = self.jwt_handler.create_token(email)

        return access_token
