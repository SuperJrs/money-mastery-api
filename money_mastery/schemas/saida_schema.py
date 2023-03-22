from datetime import date
from enum import Enum

from pydantic import BaseModel


class CategoriaEnum(str, Enum):
    lazer = 'LAZER'
    alimentacao = 'ALIMENTACAO'
    saude = 'SAUDE'
    moradia = 'MORADIA'
    transporte = 'TRANSPORTE'
    educacao = 'EDUCACAO'
    outro = 'OUTRO'


class FormaPagamentoEnum(str, Enum):
    credito = 'CREDITO'
    debito = 'DEBITO'
    pix = 'PIX'
    dinheiro = 'DINHEIRO'
    reserva = 'RESERVA'
    emprestimo = 'EMPRESTIMO'


class SaidaSchema(BaseModel):
    valor_saida: float
    categoria: CategoriaEnum
    descricao_saida: str
    forma_pagamento: FormaPagamentoEnum
    dt_hora_saida: date
    id_reserva: int

    class Config:
        orm_model = True


class SaidaSchemaFull(SaidaSchema):
    id_saida: int
    cpf_proprietario: int

