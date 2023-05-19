from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReservaSchema(BaseModel):
    dt_lembrete: date
    titulo_lembrete: str
    
    class Config:
        orm_model=True
    
class ReservaFullSchema(ReservaSchema):
    id_lembrete: str
    cpf_proprietario: str
    

class ReservaUpSchema(BaseModel):
    dt_lembrete: Optional[date]
    titulo_lembrete: Optional[str]

    class Config:
        orm_model=True
    