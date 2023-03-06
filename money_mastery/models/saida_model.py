from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Numeric,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Saida(Base):
    __tablename__ = 'saida'

    id_saida = Column(BigInteger, primary_key=True)
    valor_saida = Column(Numeric(9, 2), nullable=False)
    categoria = Column(
        Enum(
            'LAZER',
            'ALIMENTACAO',
            'SAUDE',
            'MORADIA',
            'TRANSPORTE',
            'EDUCACAO',
            'OUTRO',
            name='categoria',
        ),
        nullable=False,
    )
    descricao_saida = Column(String(100))
    forma_pagamento = Column(
        Enum(
            'CREDITO',
            'DEBITO',
            'PIX',
            'DINHEIRO',
            'RESERVA',
            'EMPRESTIMO',
            name='forma_pagamento',
        ),
        nullable=False,
    )
    dt_hora_saida = Column(DateTime, nullable=False)
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

    conta = relationship('Conta')
    reserva = relationship('Reserva')
