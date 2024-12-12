from models.database import session 
from sqlalchemy import and_,or_
from models.inventario_model import Inventario
from models.alugueis_model import Alugueis
from sqlalchemy import join
import datetime as date


class AluguelController:
    def __init__(self,session):
        self.session = session

    def listar_carros_disponiveis(self):
        
        try:
            carros_disponiveis = self.session.query(Inventario).all()
            return carros_disponiveis
        
        except Exception as e:
            print(f"Erro ao listar os carros disponiveis: {e}")
            return []

    def alugar_carro(self,clientes_id,inventario_id,valor_aluguel,data_aluguel=date.datetime.today(),data_devolucao=None):

        try:
            if not data_devolucao:
                data_devolucao = data_aluguel + date.timedelta(days=7)

            alugueis_existentes = self.session.query(Alugueis).filter(
                and_(
                    Alugueis.inventario_id == inventario_id, #verifica se ja existe um aluguel para o carro escolhido painho
                    or_(
                        and_(Alugueis.data_aluguel <= data_aluguel,
                            Alugueis.data_devolucao >= data_aluguel
                        ),
                        Alugueis.data_devolucao == None
                        )
                    )
                ).all()


            if alugueis_existentes:
                print("Já existe um aluguel para o carro selecionado, Escolha outra opção.")
                return None
            aluguel = Alugueis(
                clientes_id=clientes_id,
                inventario_id=inventario_id,
                data_aluguel=data_aluguel,
                data_devolucao=data_devolucao,
                valor_aluguel=valor_aluguel
            )
            session.add(aluguel)
            session.commit()
            print(f"Carro alugado com sucesso! Aluguel ID: {aluguel.aluguel_id}")
        
        except Exception as e:
            print(f"Ocorreu um erro ao tentar alugar um carro reveja as informações {e}")

    def lista_carros_alugados(self):
        carros_alugados = self.session.query(Alugueis,Inventario).join(Alugueis,Inventario.inventario_id == Alugueis.inventario_id).all()
        try:
            if not carros_alugados:
                print("Não a carros alugados no momento.")
            for carro_alugado,modelo in carros_alugados:
                if carro_alugado.data_devolucao == None:
                    carro_alugado.data_devolucao = "Data para devolução não encontrada!"
                print(f"O carro : {modelo.modelo_carro}  está alugado\n Data aluguel: {carro_alugado.data_aluguel}\n Data devolução: {carro_alugado.data_devolucao}")
        
        except Exception as e:
            print(f"Ocorreu um erro ao listar os carros alugados: {e}")




