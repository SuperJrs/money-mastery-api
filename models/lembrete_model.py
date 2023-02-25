from sqlalchemy import BigInteger, Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Lembrete(Base):
    __tablename__ = 'lembrete'

    id_lembrete = Column(BigInteger, primary_key=True)
    dt_lembrete = Column(Date, nullable=False)
    titulo_lembrete = Column(String(30), nullable=False)
    cpf_proprietario = Column(ForeignKey('conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)

    conta = relationship('Conta')
