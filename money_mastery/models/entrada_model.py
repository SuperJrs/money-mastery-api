from sqlalchemy import (Column, DateTime, Enum, ForeignKey, Numeric,
                        Integer, String, text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from .conta_model import Conta

Base = declarative_base()
metadata = Base.metadata


class Entrada(Base):
    __tablename__ = 'entrada'

    id_entrada = Column(Integer, primary_key=True, server_default=text("nextval('entrada_id_entrada_seq'::regclass)"))
    valor_entrada = Column(Numeric(9, 2), nullable=False)
    origem = Column(
        Enum(
            'PIX', 'SALARIO', 'EMPRESTIMO', 'RESERVA', 'OUTRO', name='origem'
        ),
        nullable=False,
    )
    descricao_entrada = Column(String(100))
    dt_hora_entrada = Column(DateTime, nullable=False)
    cpf_proprietario = Column(
        ForeignKey(
            'conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'
        ),
        nullable=False,
    )
    id_reserva = Column(
        ForeignKey(
            'reserva.id_reserva', ondelete='RESTRICT', onupdate='CASCADE'
        )
    )
    id_emprestimo = Column(
        ForeignKey(
            'emprestimo.id_emprestimo', ondelete='RESTRICT', onupdate='CASCADE'
        )
    )

    # conta = relationship('Conta')
    # emprestimo = relationship('Emprestimo')
    # reserva = relationship('Reserva')
