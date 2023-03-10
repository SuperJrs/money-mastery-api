from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ...auth.service import AuthService
from ..deps import get_current_user
from ...models.conta_model import Conta
from ...schemas.conta_schema import ContaSchema
from ..deps import get_auth_service


router = APIRouter(tags=['Login'])

@router.post('/login')
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Incorrect username or password',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    access_token = auth_service.create_access_token(str(user.email))
    
    return {'access_token': access_token, 'token_type': 'bearer'}


@router.get('/user-current', response_model=ContaSchema, status_code=200)
async def get_user_current(
    account_current: Conta = Depends(get_current_user)
):
    return account_current
