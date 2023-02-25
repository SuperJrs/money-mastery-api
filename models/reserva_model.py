from sqlalchemy import BigInteger, Column, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Reserva(Base):
    __tablename__ = 'reserva'

    id_reserva = Column(BigInteger, primary_key=True)
    dt_criacao = Column(Date, nullable=False)
    titulo_reserva = Column(String(30), nullable=False)
    descricao_reserva = Column(String(100))
    cpf_proprietario = Column(ForeignKey('conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'), nullable=False)

    conta = relationship('Conta')
