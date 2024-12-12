from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from models.database import Base

class Clientes(Base):
    __tablename__ = 'clientes'
    clientes_id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable= False)
    sobrenome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    telefone = Column(String(20), nullable=True)
