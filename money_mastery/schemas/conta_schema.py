from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class ContaSchema(BaseModel):
    cpf_proprietario: int
    nome_proprietario: str
    dt_nasc_proprietario: date
    telefone: Optional[int]
    email: EmailStr

    class Config:
        orm_mode = True
        

class ContaSchemaFull(ContaSchema):
    senha: str


class ContaSchemaOptional(BaseModel):
    nome_proprietario: Optional[str]
    dt_nasc_proprietario: Optional[date]
    telefone: Optional[int]

    class Config:
        orm_mode = True
