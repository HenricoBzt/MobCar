
from models.clientes_model import Clientes


class ClienteController:
    def __init__(self,session):
        self.session = session
    def cadastrar_cliente(self,nome,sobrenome,endereco,telefone,session):
        
        cliente = Clientes(
            nome=nome,
            sobrenome=sobrenome,
            endereco=endereco,
            telefone = telefone)
        
        
        session.add(cliente)
        session.commit()
        print(f"Cliente {cliente.nome}, {cliente.sobrenome} cadastrado com sucesso!")





