from sqlalchemy import Column,Integer,Date,DECIMAL,ForeignKey
from sqlalchemy.orm import relationship
from models.database import Base
 
class Alugueis(Base):
    __tablename__ = 'alugueis'

    aluguel_id = Column(Integer, primary_key=True)
    clientes_id = Column(Integer, ForeignKey('clientes.clientes_id'))
    inventario_id = Column(Integer, ForeignKey('inventario.inventario_id'))
    data_aluguel = Column(Date, nullable=False)
    data_devolucao = Column(Date, nullable=True)
    valor_aluguel = Column(DECIMAL(10,2), default=0.00)

   

