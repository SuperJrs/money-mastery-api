from fastapi import APIRouter, Depends, status
from databases.interfaces import Record
from datetime import datetime
from typing import Any

from ...core.database import database
from ...schemas.entrada_schema import EntradaSchema, EntradaSchemaFull, EntradaSchemaUp
from ...models.entrada_model import Entrada
from ...models.conta_model import Conta
from ..deps import get_current_user

from sqlalchemy import insert, select, update, delete, and_


router: APIRouter = APIRouter(prefix='/entrada', tags=['Entrada em conta'])

@router.post(
    '/',
    status_code=201,
    description='Gerar nova entrada',
    response_model=EntradaSchemaFull
)
async def add_entrada(
    entrada: EntradaSchema,
    current_user: Conta = Depends(get_current_user),
):
    entrada_dict = entrada.dict()
    entrada_dict['cpf_proprietario'] = current_user.cpf_proprietario
    id_entrada = await database.execute(insert(Entrada).values(**entrada_dict))
    entrada_dict['id_entrada'] = id_entrada
    
    return EntradaSchemaFull(**entrada_dict)


@router.get(
    '/',
    description='Obtem todas entradas recebidas em um periodo',
    response_model=list[EntradaSchemaFull]
)
async def get_entradas(
    dt_inicio: str,
    dt_final: str,
    current_user: Conta = Depends(get_current_user)
):
    query = select(Entrada).where(
        and_(
            Entrada.cpf_proprietario == current_user.cpf_proprietario,
            Entrada.dt_hora_entrada.between(
                datetime.strptime(dt_inicio, '%d/%m/%Y'), 
                datetime.strptime(dt_final, '%d/%m/%Y')
            )
        )
    )
    entradas: list[Record] = await database.fetch_all(query)
    
    return entradas


@router.get(
    '/{id_entrada}',
    description='Obtem uma entrada especifica',
    response_model=EntradaSchemaFull,
    status_code=status.HTTP_200_OK
)
async def get_entrada(
    id_entrada: int,
    current_user: Conta = Depends(get_current_user)
):
    return await database.fetch_one(
        select(Entrada).where(
            and_(
                Entrada.cpf_proprietario == current_user.cpf_proprietario,
                Entrada.id_entrada == id_entrada
            )
        )
    )


@router.put(
    '/{id_entrada}',
    description='Edita uma entrada',
    response_model=EntradaSchemaFull,
    status_code=status.HTTP_202_ACCEPTED    
)
async def alterar_entrada(
    id_entrada: int,
    entrada_alterada: EntradaSchemaUp,
    current_user: Conta = Depends(get_current_user)
):
    entrada_alterada_dict: dict[str, Any] = entrada_alterada.dict()
    up_entrada = update(Entrada).where(
        and_(
            Entrada.cpf_proprietario == current_user.cpf_proprietario,
            Entrada.id_entrada == id_entrada
        )
    ).values(**{
        key: entrada_alterada_dict[key] 
        for key in entrada_alterada_dict if entrada_alterada_dict[key]
    })
    
    await database.execute(up_entrada)
    
    return await database.fetch_one(
        select(Entrada).where(
            and_(
                Entrada.cpf_proprietario == current_user.cpf_proprietario,
                Entrada.id_entrada == id_entrada
            )
        )
    )


@router.delete(
    '/{id_entrada}',
    description='Apaga uma entrada',
    status_code=status.HTTP_202_ACCEPTED
)
async def delete_entrada(
    id_entrada: int,
    current_user: Conta = Depends(get_current_user)
):
    await database.execute(
        delete(Entrada).where(
            and_(
                Entrada.cpf_proprietario == current_user.cpf_proprietario,
                Entrada.id_entrada == id_entrada
            )
        )
    )
    return dict(msg='Entrada apagada!')
