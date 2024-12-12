
from sqlalchemy import Column,Integer,String,ForeignKey
from models.database import Base

class Inventario(Base):
    __tablename__ = 'inventario'
    inventario_id = Column(Integer,primary_key=True)
    modelo_carro = Column(String(255), nullable= False)
    transmissao = Column(String(255), nullable= False)
    motor = Column(String(255), nullable= False)
    combustivel = Column(String(255), nullable= False)
    marcas_id = Column(Integer,ForeignKey('marcas.marcas_id'))
