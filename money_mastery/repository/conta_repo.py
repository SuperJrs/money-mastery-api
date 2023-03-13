from databases import Database
from databases.interfaces import Record
from fastapi import HTTPException, status
from sqlalchemy import delete, insert, select, update

from ..auth.crypt import hash_password
from ..models.conta_model import Conta
from ..schemas.conta_schema import ContaSchemaFull, ContaSchemaOptional


class ContaRepo:
    def __init__(self, database: Database):
        self.database = database

    async def create(self, nova_conta: ContaSchemaFull):
        try:
            nova_conta.senha = hash_password(nova_conta.senha)
            insert_conta = insert(Conta).values(**nova_conta.dict())
            await self.database.execute(insert_conta)

        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)
        conta: Record = await self.get_by_cpf(nova_conta.cpf_proprietario)
        return conta

    async def gel_all(self):
        try:
            contas: list[Record] = await self.database.fetch_all(select(Conta))
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
            conta: Record | None = await self.database.fetch_one(query)
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
            conta: Record | None = await self.database.fetch_one(query)
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
            conta: Record | None = await self.database.fetch_one(query)
            if conta:
                print(conta)
                delete_sql = delete(Conta).where(Conta.cpf_proprietario == cpf)
                await self.database.execute(delete_sql)
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Conta não encontrada!',
                status_code=404,
            )

        return {'msg': 'Conta apagada com sucesso!'}

    async def update(self, cpf: int, conta_alterada: ContaSchemaOptional):
        print()
        try:
            conta_alterada_dict: dict = conta_alterada.dict()

            for key in conta_alterada.dict():
                if not conta_alterada_dict[key]:
                    del conta_alterada_dict[key]

            update_conta = (
                update(Conta)
                .where(Conta.cpf_proprietario == cpf)
                .values(**conta_alterada_dict)
            )

            await self.database.execute(update_conta)
            conta: Record = await self.get_by_cpf(cpf)
        except Exception as err:
            raise HTTPException(status_code=500, detail=err)
        return conta
