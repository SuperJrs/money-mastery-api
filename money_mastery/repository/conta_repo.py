from fastapi import HTTPException, status
from sqlalchemy import select, insert, delete

from ..core.database import database
from ..models.conta_model import Conta
from ..schemas.conta_schema import ContaSchema


class ContaRepo:
    @staticmethod
    async def create(nova_conta: ContaSchema):
        try:
            insert_conta = insert(Conta).values(**nova_conta.dict())
            await database.execute(insert_conta)
            
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)
        return nova_conta

    @staticmethod
    async def gel_all():
        try:
            contas = await database.fetch_all(select(Conta))
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not contas:
            raise HTTPException(
                detail='Não a contas para retornar',
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return contas
    
    @staticmethod
    async def get_by_cpf(cpf: int):
        try:
            query = select(Conta).where(Conta.cpf_proprietario == cpf)
            conta = await database.fetch_one(query)
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Não existe nenhuma conta onde o proprietario possui o cpf={cpf}',
                status_code=404,
            )
            
        return conta
    
    @staticmethod
    async def destroy(cpf: int):
        try:
            query = select(Conta).where(Conta.cpf_proprietario == cpf)
            conta = await database.fetch_one(query)
            nome_proprietario = ''
            if conta:
                nome_proprietario = conta.nome_proprietario  # type: ignore
                print(conta)
                delete_sql = delete(Conta).where(Conta.cpf_proprietario == cpf)
                await database.execute(delete_sql)
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Não existe nenhuma conta onde o proprietario possui o cpf={cpf}',
                status_code=404,
            )

        return {
            'msg': f'conta do(a) {nome_proprietario} foi deletada com sucesso'
        }
