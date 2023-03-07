from fastapi import APIRouter, status

from ..repository.conta_repo import ContaRepo
from ..schemas.conta_schema import ContaSchema

router = APIRouter(prefix='/conta')
repo = ContaRepo()


@router.get('/', response_model=list[ContaSchema])
async def obter_contas():
    result = await repo.gel_all()
    return result


@router.get(
    '/{cpf}', 
    response_description='Obtem uma conta através do CPF do proprietario',
    response_model=ContaSchema,
    status_code=200
)
async def obter_conta(cpf: int):
    return await repo.get_by_cpf(cpf)


@router.post(
    '/', response_model=ContaSchema, status_code=status.HTTP_201_CREATED
)
async def adicionar_nova_conta(nova_conta: ContaSchema):
    return await repo.create(nova_conta)


@router.delete('/{cpf}', status_code=status.HTTP_202_ACCEPTED)
async def deletar_conta(cpf: int):
    return await repo.destroy(cpf)
