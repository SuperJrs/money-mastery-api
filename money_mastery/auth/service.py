from typing import Optional

from ..core.configs import settings
from ..core.database import database
from ..models.conta_model import Conta
from ..repository.conta_repo import ContaRepo
from .crypt import check_password
from .jwt_handler import JWTHandler


def get_conta_repo() -> ContaRepo:
    return ContaRepo(database)


def get_jwt_handler() -> JWTHandler:
    return JWTHandler(settings.KEY_JWT)


class AuthService:
    def __init__(
        self,
        conta_repository: ContaRepo = ContaRepo(database),
        jwt_handler: JWTHandler = JWTHandler(settings.KEY_JWT),
    ):
        self.conta_repository = conta_repository
        self.jwt_handler = jwt_handler

    async def authenticate_user(
        self, email: str, password: str
    ) -> Optional[Conta]:
        conta = await self.conta_repository.get_by_email(email)

        if conta and check_password(password, conta.senha):   # type: ignore
            return conta   # type: ignore

        return None

    def create_access_token(self, email: str) -> str:
        access_token = self.jwt_handler.create_token(email)

        return access_token
