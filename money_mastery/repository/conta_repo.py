from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.conta_model import Conta
from schemas.conta_schema import ContaSchema


class ContaRepo:
    @staticmethod
    def create(nova_conta: ContaSchema, db: Session):
        try:
            conta = Conta(
                cpf_proprietario=nova_conta.cpf_proprietario,
                nome_proprietario=nova_conta.nome_proprietario,
                dt_nasc_proprietario=nova_conta.dt_nasc_proprietario,
                telefone=nova_conta.telefone,
                email=nova_conta.email,
                senha=nova_conta.senha,
            )

            db.add(conta)
            db.commit()
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)
        return conta

    @staticmethod
    def gel_all(db: Session):
        try:
            contas = db.query(Conta).all()
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not contas:
            raise HTTPException(
                detail='Não a contas para retornar',
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return contas

    @staticmethod
    def destroy(cpf: int, db: Session):
        try:
            conta = (
                db.query(Conta).filter(Conta.cpf_proprietario == cpf).first()
            )
            nome_proprietario = ''
            if conta:
                nome_proprietario = conta.nome_proprietario
                db.delete(conta)
                db.commit()
        except Exception as err:
            raise HTTPException(detail=str(err), status_code=500)

        if not conta:
            raise HTTPException(
                detail=f'Não existe nenhuma conta onde o proprietario possui o cpf={cpf}',
                status_code=404,
            )

        return {
            'msg': f'conta do {nome_proprietario} foi deletada com sucesso'
        }
