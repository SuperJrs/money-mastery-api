from sqlalchemy import BigInteger, Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Lembrete(Base):
    __tablename__ = 'lembrete'

    Column(Integer, primary_key=True, server_default=text("nextval('lembrete_id_lembrete_seq'::regclass)"))
    dt_lembrete = Column(Date, nullable=False)
    titulo_lembrete = Column(String(30), nullable=False)
    cpf_proprietario = Column(
        ForeignKey(
            'conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'
        ),
        nullable=False,
    )

    conta = relationship('Conta')
