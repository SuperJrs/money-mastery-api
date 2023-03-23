from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class GastoBase(Base):
    __tablename__ = 'gasto_base'

    id_gasto_base = Column(Integer, primary_key=True, server_default=text("nextval('gasto_base_id_gasto_base_seq'::regclass)"))
    titulo_gasto = Column(String(30), nullable=False)
    valor_gasto = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(
        ForeignKey(
            'conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'
        ),
        nullable=False,
    )

    # conta = relationship('Conta')
