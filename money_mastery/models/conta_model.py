from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    Date,
    String
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Conta(Base):
    __tablename__ = 'conta'
    __table_args__ = (
        CheckConstraint("(telefone IS NULL) OR (telefone <= '99999999999'::bigint)"),
        CheckConstraint("cpf_proprietario <= '99999999999'::bigint")
    )

    cpf_proprietario = Column(BigInteger, primary_key=True)
    nome_proprietario = Column(String(120), nullable=False)
    dt_nasc_proprietario = Column(Date, nullable=False)
    telefone = Column(BigInteger)
    email = Column(String(90), nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
