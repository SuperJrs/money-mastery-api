from databases.interfaces import Record
from fastapi import APIRouter, status

from ...core.database import database
from ...repository.conta_repo import ContaRepo
from ...schemas.conta_schema import ContaSchema, ContaSchemaOptional

router: APIRouter = APIRouter(prefix='/conta', tags=['Admin'])
repo: ContaRepo = ContaRepo(database)


@router.get('/', response_model=list[ContaSchema])
async def obter_contas():
    result: list[Record] = await repo.gel_all()
    return result


@router.get(
    '/{cpf}',
    response_description='Obtem uma conta através do CPF do proprietario',
    response_model=ContaSchema,
    status_code=200,
)
async def obter_conta(cpf: int):
    return await repo.get_by_cpf(cpf)


@router.put(
    '/{cpf}',
    response_model=ContaSchema,
    response_description='Atualiza a conta de um usuario',
)
async def alterar_conta(cpf: int, conta_alterada: ContaSchemaOptional):
    return await repo.update(cpf, conta_alterada)


@router.delete(
    '/{cpf}',
    status_code=status.HTTP_202_ACCEPTED,
    response_description='Deletar uma conta',
)
async def deletar_conta(cpf: int):
    return await repo.destroy(cpf)
