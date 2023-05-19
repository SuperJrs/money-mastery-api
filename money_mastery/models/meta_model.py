from sqlalchemy import BigInteger, Column, ForeignKey, Integer, Numeric, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Meta(Base):
    __tablename__ = 'meta'

    id_meta = Column(Integer, primary_key=True, server_default=text("nextval('meta_id_meta_seq'::regclass)"))
    valor_meta = Column(Numeric(9, 2), nullable=False)
    cpf_proprietario = Column(
        ForeignKey(
            'conta.cpf_proprietario', ondelete='CASCADE', onupdate='RESTRICT'
        ),
        nullable=False,
    )

    conta = relationship('Conta')
