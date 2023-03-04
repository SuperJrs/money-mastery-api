from sqlalchemy import BigInteger, Column, ForeignKey, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GastoBase(Base):
    __tablename__ = 'gasto_base'

    id_gasto_base = Column(BigInteger, primary_key=True)
    titulo_gasto = Column(String(30), nullable=False)
    valor_gasto = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(ForeignKey('conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)

    conta = relationship('Conta')
