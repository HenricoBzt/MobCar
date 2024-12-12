from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from models.database import Base
 
class Marcas(Base):
    __tablename__ = 'marcas'
    marcas_id = Column(Integer, primary_key=True)
    nome_marca = Column(String(255), nullable=False)
    origem = Column(String(255), nullable= True)

