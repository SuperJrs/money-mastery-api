from fastapi import APIRouter, Depends, HTTPException, status
from models.conta_model import Conta
from core.deps import get_session
from schemas.conta_schema import ContaSchema


router = APIRouter(prefix="/conta")


@router.get("/", response_model=list[ContaSchema])
def obter_contas(db=Depends(get_session)):
    result = db.query(Conta).all()
    return result


@router.post("/", response_model=ContaSchema)
def adicionar_nova_conta(nova_conta: ContaSchema, db=Depends(get_session)):
    conta = Conta(
        cpf_proprietario=nova_conta.cpf_proprietario,
        nome_proprietario=nova_conta.nome_proprietario,
        dt_nasc_proprietario=nova_conta.dt_nasc_proprietario,
        telefone=nova_conta.telefone,
        email=nova_conta.email,
        senha=nova_conta.senha
    )

    db.add(conta)
    db.commit()

    return conta


@router.delete("/{cpf}")
def deletar_conta(cpf: int, db=Depends(get_session)):

    conta_a_deletar = db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()

    if not conta_a_deletar:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="A conta não foi encontrada"
        )

    db.delete(conta_a_deletar)
    db.commit()

    return {"detail": "A conta foi apaga com sucesso"}


