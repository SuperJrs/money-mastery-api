from fastapi import APIRouter, Depends, status
from databases.interfaces import Record
from datetime import datetime
from typing import Any
from sqlalchemy import insert, select, update, delete, and_

from ...core.database import database
from ...schemas.saida_schema import SaidaSchema, SaidaSchemaFull, SaidaSchemaUp
from ...models.saida_model import Saida
from ...models.conta_model import Conta
from ..deps import get_current_user


router: APIRouter = APIRouter(prefix='/saida', tags=['Saida em conta'])

@router.post(
    '/',
    description='Adiciona uma nova saida na conta do usuario logado',
    status_code=201,
    response_model=SaidaSchemaFull,
)
async def add_saida(saida: SaidaSchema, user: Conta = Depends(get_current_user)):
    saida_dict: dict[str, Any] = saida.dict()
    saida_dict['cpf_proprietario'] = user.cpf_proprietario
    
    id_saida = await database.execute(insert(Saida).values(**saida_dict))
    saida_dict['id_saida'] = id_saida
    
    return saida_dict


@router.get(
    '/{id_saida}',
    description='Obtem uma saida especifica',
    status_code=200,
    response_model=SaidaSchemaFull
)
async def get_saida(id_saida: int, user: Conta = Depends(get_current_user)):
    return await database.fetch_one(
        select(Saida).where(
            and_(
                Saida.id_saida == id_saida,
                Saida.cpf_proprietario == user.cpf_proprietario
            )
        )
    )


@router.put(
    '/{id_saida}',
    description='Altera uma saida especifica',
    status_code=status.HTTP_202_ACCEPTED,
    response_model=SaidaSchemaFull
)
async def update_saida(
    id_saida: int, 
    saida: SaidaSchemaUp, 
    user: Conta = Depends(get_current_user)
):
    saida_dict: dict[str, Any] = saida.dict()
    await database.execute(update(Saida).where(
        and_(
            Saida.id_saida == id_saida,
            Saida.cpf_proprietario == user.cpf_proprietario
        )
    ).values(**{
            key: saida_dict[key] for key in saida_dict if saida_dict[key] 
    }))
    
    return await database.fetch_one(
        select(Saida).where(
            and_(
                Saida.id_saida == id_saida,
                Saida.cpf_proprietario == user.cpf_proprietario
            )
        )
    )


@router.delete(
    '/{id_saida}',
    description='Apaga uma saida',
    status_code=status.HTTP_202_ACCEPTED,
)
async def delete_saida(id_saida: int, user: Conta = Depends(get_current_user)):
    await database.execute(
        delete(Saida).where(
            and_(
                Saida.id_saida == id_saida,
                Saida.cpf_proprietario == user.cpf_proprietario
            )
        )
    )
    
    return dict(msg='Saida apagado com sucesso!')
