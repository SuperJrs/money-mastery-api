from enum import Enum
from datetime import date
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
    id_saida: int
    valor_saida: float
    categoria: CategoriaEnum
    descricao_saida: str
    forma_pagamento: FormaPagamentoEnum
    dt_hora_saida: date
    cpf_proprietario: int
    id_reserva: int
    
    class Config:
        orm_model = True
