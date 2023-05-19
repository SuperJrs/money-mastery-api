from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReservaSchema(BaseModel):
    titulo_reserva: str
    descricao_reserva: str
    
    class Config:
        orm_model=True
    
class ReservaFullSchema(ReservaSchema):
    id_reserva: str
    dt_criacao: date
    cpf_proprietario: str
    

class ReservaUpSchema(BaseModel):
    titulo_reserva: Optional[str]
    descricao_reserva: Optional[str]

    class Config:
        orm_model=True