from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from models.database import Base
from datetime import datetime,date
class Pagamentos(Base):
    __tablename__ = 'pagamentos'
    pagamento_id = Column(Integer,primary_key=True)
    clientes_id = Column(Integer,ForeignKey('clientes.clientes_id'))
    aluguel_id = Column(Integer,ForeignKey('aluguel.alugel_id'))
    metodo_pagamento = Column(String(40),nullable= False )
    data_hora_pagamento = Column(DateTime, nullable=False)

