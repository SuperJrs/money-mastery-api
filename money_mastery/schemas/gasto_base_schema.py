from typing import Optional
from pydantic import BaseModel


class GastoBaseSchema(BaseModel):
    titulo_gasto: str
    valor_gasto: float
    
    class Config:
        orm_model=True
        

class GastoBaseFullSchema(GastoBaseSchema):
    id_gasto_base: int
    cpf_proprietario: int


class GastoBaseUpSchema(BaseModel):
    titulo_gasto: Optional[str]
    valor_gasto: Optional[float]
