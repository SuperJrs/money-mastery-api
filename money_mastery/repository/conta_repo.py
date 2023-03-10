from fastapi import HTTPException, status
from databases import Database
from sqlalchemy import select, insert, delete

# from ..core.database import database
from ..models.conta_model import Conta
from ..schemas.conta_schema import ContaSchema
from ..auth.crypt import hash_password


class ContaRepo:
    def __init__(self, database: Database):
        self.database = database
    
    async def create(self, nova_conta: ContaSchema):
        try:
            nova_conta.senha = hash_password(nova_conta.senha)
            insert_conta = insert(Conta).values(**nova_conta.dict())
            await self.database.execute(insert_conta)
            
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)
        return nova_conta

    async def gel_all(self):
        try:
            contas = await self.database.fetch_all(select(Conta))
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not contas:
            raise HTTPException(
                detail='Não a contas para retornar',
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return contas
    
    async def get_by_cpf(self, cpf: int):
        try:
            query = select(Conta).where(Conta.cpf_proprietario == cpf)
            conta = await self.database.fetch_one(query)
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Não existe nenhuma conta onde o proprietario possui o cpf={cpf}',
                status_code=404,
            )
            
        return conta
    
    async def get_by_email(self, email_conta: str):
        try:
            query = select(Conta).where(Conta.email == email_conta)
            conta = await self.database.fetch_one(query)
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Não existe nenhuma conta com esse email',
                status_code=404,
            )
            
        return conta
    
    async def destroy(self, cpf: int):
        try:
            query = select(Conta).where(Conta.cpf_proprietario == cpf)
            conta = await self.database.fetch_one(query)
            nome_proprietario = ''
            if conta:
                nome_proprietario = conta.nome_proprietario  # type: ignore
                print(conta)
                delete_sql = delete(Conta).where(Conta.cpf_proprietario == cpf)
                await self.database.execute(delete_sql)
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
