from fastapi import APIRouter, Depends, status

from ..core.deps import get_session
from ..repository.conta_repo import ContaRepo
from ..schemas.conta_schema import ContaSchema

router = APIRouter(prefix='/conta')
repo = ContaRepo()


@router.get('/', response_model=list[ContaSchema])
def obter_contas(db=Depends(get_session)):
    result = repo.gel_all(db)
    return result


@router.get(
    '/{cpf}', 
    response_description='Obtem uma conta através do CPF do proprietario',
    status_code=200
)
def obter_conta(cpf: int, db=Depends(get_session)) -> ContaSchema:
    return repo.get_by_cpf(cpf, db)


@router.post(
    '/', response_model=ContaSchema, status_code=status.HTTP_201_CREATED
)
def adicionar_nova_conta(nova_conta: ContaSchema, db=Depends(get_session)):
    return repo.create(nova_conta, db)


@router.delete('/{cpf}', status_code=status.HTTP_202_ACCEPTED)
def deletar_conta(cpf: int, db=Depends(get_session)):
    result = repo.destroy(cpf, db)
    return result
