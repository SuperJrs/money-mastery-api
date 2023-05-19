from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Origem(str, Enum):
    pix = 'PIX'
    salario = 'SALARIO'
    emprestimo = 'EMPRESTIMO'
    reserva = 'RESERVA'
    outro = 'OUTRO'    


class EntradaSchema(BaseModel):
    valor_entrada: float
    origem: Origem
    descricao_entrada: Optional[str]
    dt_hora_entrada: datetime
    id_reserva: Optional[int]
    id_emprestimo: Optional[int]
    
    class Config:
        orm_model=True


class EntradaSchemaFull(EntradaSchema):
    id_entrada: int
    cpf_proprietario: int


class EntradaSchemaUp(BaseModel):
    valor_entrada: Optional[float]
    origem: Optional[Origem]
    descricao_entrada: Optional[str]
    dt_hora_entrada: Optional[datetime]
    id_reserva: Optional[int]
    id_emprestimo: Optional[int]
    

