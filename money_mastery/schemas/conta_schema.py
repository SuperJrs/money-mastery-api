from datetime import date
from typing import Optional

from pydantic import BaseModel


class ContaSchema(BaseModel):
    cpf_proprietario: int
    nome_proprietario: str
    dt_nasc_proprietario: date
    telefone: Optional[int]
    email: str
    senha: str

    class Config:
        orm_mode = True
