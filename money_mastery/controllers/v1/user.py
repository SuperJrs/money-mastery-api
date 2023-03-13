from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ...auth.service import AuthService
from ...core.database import database
from ...models.conta_model import Conta
from ...repository.conta_repo import ContaRepo
from ...schemas.conta_schema import ContaSchema, ContaSchemaOptional, ContaSchemaFull
from ..deps import get_auth_service, get_current_user

router = APIRouter(prefix='/user', tags=['Usuário'])
repo = ContaRepo(database)


@router.post('/login', status_code=200)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
):
    user = await auth_service.authenticate_user(
        form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token = auth_service.create_access_token(str(user.email))

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post(
    '/register',
    response_model=ContaSchema,
    response_description='Criar conta',
    status_code=status.HTTP_201_CREATED,
)
async def adicionar_nova_conta(nova_conta: ContaSchemaFull):
    return await repo.create(nova_conta)


@router.get('/me', response_model=ContaSchema, status_code=200)
async def get_user_current(account_current: Conta = Depends(get_current_user)):
    return account_current


@router.put(
    '/',
    response_model=ContaSchema,
    response_description='Atualizar conta',
    status_code=status.HTTP_202_ACCEPTED
)
async def alterar_conta(
    conta_alterada: ContaSchemaOptional,
    account_current: Conta = Depends(get_current_user),
):
    return await repo.update(
        account_current.cpf_proprietario, conta_alterada # type: ignore
    )   


@router.delete(
    '/',
    status_code=status.HTTP_202_ACCEPTED,
    response_description='Deletar uma conta',
)
async def deletar_conta(account_current: Conta = Depends(get_current_user)):
    return await repo.destroy(
        account_current.cpf_proprietario # type: ignore
    )   
