from models.database import session 
from sqlalchemy import and_,or_
from models.inventario_model import Inventario
from models.marcas_model import Marcas

class InventarioController:
    def __init__(self,session):
        self.session = session

    def listar_carros_disponiveis(self):
        
        try:
            carros_disponiveis = self.session.query(Inventario).all()
            return carros_disponiveis
        
        except Exception as e:
            print(f"Erro ao listar os carros disponiveis: {e}")
            return []

    def buscar_carro_especifico(self):
        pass

