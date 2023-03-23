from sqlalchemy import Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Reserva(Base):
    __tablename__ = 'reserva'

    id_reserva = Column(Integer, primary_key=True, server_default=text("nextval('reserva_id_reserva_seq'::regclass)"))
    dt_criacao = Column(Date, nullable=False)
    titulo_reserva = Column(String(30), nullable=False)
    descricao_reserva = Column(String(100))
    cpf_proprietario = Column(
        ForeignKey(
            'conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'
        ),
        nullable=False,
    )

    # conta = relationship('Conta')
