from sqlalchemy import BigInteger, Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    id_emprestimo = Column(BigInteger, primary_key=True)
    nome_devedor = Column(String(120), nullable=False)
    dt_emprestimo = Column(Date, nullable=False)
    dt_limite_pg = Column(Date)
    cpf_proprietario = Column(ForeignKey('conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)
    id_saida = Column(ForeignKey('saida.id_saida', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    conta = relationship('Conta')
    saida = relationship('Saida')