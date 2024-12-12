from tkinter import *
from tkinter import ttk
from controllers.clientes_controller import ClienteController
from controllers.alugueis_controller import AluguelController
from controllers.inventario_controller import InventarioController
from models.database import session
root = Tk() #Cria uma janela.

class Funcs():
    def limpar_credencias(self):
        self.codigo_entry_nome.delete(0,END)
        self.codigo_entry_sobrenome.delete(0,END)
        self.codigo_entry_endereco.delete(0,END)
        self.codigo_entry_telefone.delete(0,END)
    def cadastro(self):
        nome = self.codigo_entry_nome.get()
        sobrenome = self.codigo_entry_sobrenome.get()
        endereco = self.codigo_entry_endereco.get()
        telefone = self.codigo_entry_telefone.get()

        try:
            controller = ClienteController(session)
            # if not nome  and not sobrenome  and not endereco  and not telefone :
            #     self.mensagem["text"] = "Preencha todos os campos."
            controller.cadastrar_cliente(nome,sobrenome,endereco,telefone,session)
            self.mensagem["text"] = "Cliente cadastrado com sucesso!"
            self.limpar_credencias()
        
        except Exception as e:
            self.mensagem["text"] = f"Erro ao cadastrar um cliente {e}"

    def listar_carros(self):
        try:
            inventario_controle = InventarioController(session)
            lista = inventario_controle.listar_carros_disponiveis()

            for item in self.listaCli.get_children():
                self.listaCli.delete(item)
            
            for carro in lista:
                self.listaCli.insert("",END,values=(
                    carro.inventario_id,
                    carro.modelo_carro, 
                    carro.transmissao, 
                    carro.motor, 
                    carro.combustivel,
                    ))
                
            self.mensagem["text"] = " Exibindo Lista de carros!"
            
        except Exception as e:
            print(f"Ocorreu um erro ao listar os carros: {e}")
    
    def abrir_janela2(self):

        self.janela2 = Toplevel()
        self.janela2.title('Alugar Carros')
        self.janela2.configure(bg='#003366')
        self.janela2.geometry('700x350')

        self.frame2 = Frame(self.janela2,bd=75,bg='#BC8F8F',
                            highlightbackground='black',highlightthickness=2)
        self.frame2.place(relx=0.02,rely=0.02,relheight=0.95,relwidth=0.96)

        self.cliente_id_label = Label(self.frame2,text='ID do Cliente',bg='#9370DB')
        self.cliente_id_label.place(relx=0.01,rely=0.03,relheight=0.1,relwidth=0.2)

        self.cliente_id_entry = Entry(self.frame2)
        self.cliente_id_entry.place(relx=0.01,rely=0.2,relheight=0.1,relwidth=0.1)

        self.inventario_id_label = Label(self.frame2,text= 'ID do Inventario')
        self.inventario_id_label.place(relx=0.01,rely=0.35,relheight=0.1,relwidth=0.2)

        self.inventario_id_entry = Entry(self.frame2)
        self.inventario_id_entry.place(relx=0.01,rely=0.5,relheight=0.1,relwidth=0.1)

        self.inventario_valor_label = Label(self.frame2,text= 'Valor do Aluguel')
        self.inventario_valor_label.place(relx=0.01,rely=0.65,relheight=0.1,relwidth=0.2)

        self.inventario_valor_entry = Entry(self.frame2)
        self.inventario_valor_entry.place(relx=0.01,rely=0.77,relheight=0.1,relwidth=0.1)

        self.inventario_dtaluguel_label = Label(self.frame2,text= 'Data do aluguel')
        self.inventario_dtaluguel_label.place(relx=0.3,rely=0.03,relheight=0.1,relwidth=0.2)

        self.inventario_dtaluguel_entry = Entry(self.frame2)
        self.inventario_dtaluguel_entry.place(relx=0.3,rely=0.2,relheight=0.1,relwidth=0.15)

        self.inventario_devolucao_label = Label(self.frame2,text='Data de Devolução')
        self.inventario_devolucao_label.place(relx=0.3,rely=0.35,relheight=0.1,relwidth=0.2)

        self.inventario_devolucao_entry = Entry(self.frame2)
        self.inventario_devolucao_entry.place(relx=0.3,rely=0.5,relheight=0.1,relwidth=0.15)

        self.bt_confirmar = Button(self.frame2,text="Cadastrar",bd=2,bg='#006400',command=self.cadastrar_aluguel)
        self.bt_confirmar.place(relx=0.3,rely=0.77,relheight=0.1,relwidth=0.2)

    def cadastrar_aluguel(self):
        try:
            cliente_id = int(self.cliente_id_entry.get())
            inventario_id = int(self.inventario_id_entry.get())
            valor_aluguel = float(self.inventario_valor_entry.get())
            data_aluguel = self.inventario_dtaluguel_entry.get()
            data_devolucao = self.inventario_devolucao_entry.get()

     
            aluguel_controller = AluguelController(session)
            aluguel_controller.alugar_carro(cliente_id, inventario_id, valor_aluguel, data_aluguel, data_devolucao)

            self.mensagem["text"] = "Carro alugado com sucesso!"
            self.janela2.destroy()

        except ValueError:
            self.mensagem["text"] = "Por favor, preencha os campos corretamente (IDs devem ser números inteiros, valor deve ser numérico)."
        except Exception as e:
            self.mensagem["text"] = f"Erro ao alugar carro: {e}"
        


class Aplicacao(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.objetos_frame1()
        self.objetos_frame2()
        root.mainloop()
        

    def tela(self):
        self.root.title('Locadora MobCar')
        self.root.configure(bg='#003366')
        self.root.geometry('990x500')
        self.root.resizable(True,True)
        self.root.minsize(width=400,height=300)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=75,bg='#BC8F8F',
                             highlightbackground='black',highlightthickness=2)
        self.frame_1.place(relx=0.02,rely=0.02,relheight=0.95,relwidth=0.96)

    def objetos_frame1(self):

        self.bt_alugar = Button(self.frame_1,text="Alugar",bd=2,bg='#FFA500', command=self.abrir_janela2)
        self.bt_alugar.place(relx=0.38,rely=0.0,relheight=0.1,relwidth=0.2)

        # Buscar alugueis disponiveis
        self.lb_buscar_id = Label(self.frame_1,text='ID',bg='#F5F5DC')
        self.lb_buscar_id.place(relx=0.8,rely=0.0,relheight=0.1,relwidth=0.05)

        self.entry_buscar_id = Entry(self.frame_1)
        self.entry_buscar_id.place(relx=0.84,rely=0.0,relheight=0.1,relwidth=0.07)
        
        self.bt_buscar = Button(self.frame_1,text="Buscar",bd=2,bg='#FFA500')
        self.bt_buscar.place(relx=0.8,rely=0.2,relheight=0.1,relwidth=0.1)

        # Listar Carros Alugados

        self.bt_listar = Button(self.frame_1,text="Listar",bd=2,bg='#FFA500',command=self.listar_carros)
        self.bt_listar.place(relx=0.59,rely=0.0,relheight=0.1,relwidth=0.2)

        self.bt_cadastrar = Button(self.frame_1,text="Cadastrar",bd=2,bg='#006400',command=self.cadastro)
        self.bt_cadastrar.place(relx=0.84,rely=0.79,relheight=0.1,relwidth=0.2)

        #Limpar dados inseridos no cadastro
        self.bt_limpar = Button(self.frame_1,text='Limpar',bd=2,bg='#FFA500',command=self.limpar_credencias )
        self.bt_limpar.place(relx=0.73,rely=0.79,relheight=0.1,relwidth=0.1)

        #criação da label entrada do codigo
        self.lb_codigo_nome = Label(self.frame_1,text="Nome",bg='#F5F5DC')
        self.lb_codigo_nome.place(relx=0.0,rely=0.3,relheight=0.09,relwidth=0.075)

        self.codigo_entry_nome = Entry(self.frame_1)
        self.codigo_entry_nome.place(relx=0.0,rely=0.45,relheight=0.1,relwidth=0.25)

        self.lb_codigo_sobrenome = Label(self.frame_1,text="Sobrenome",bg='#F5F5DC')
        self.lb_codigo_sobrenome.place(relx=0.0,rely=0.67,relheight=0.09,relwidth=0.075)

        self.codigo_entry_sobrenome = Entry(self.frame_1)
        self.codigo_entry_sobrenome.place(relx=0.0,rely=0.79,relheight=0.1,relwidth=0.30)

        self.lb_codigo_endereco = Label(self.frame_1,text="Endereço",bg='#F5F5DC')
        self.lb_codigo_endereco.place(relx=0.45,rely=0.3,relheight=0.09,relwidth=0.075)

        self.codigo_entry_endereco = Entry(self.frame_1)
        self.codigo_entry_endereco.place(relx=0.45,rely=0.45,relheight=0.1,relwidth=0.25)

        self.lb_codigo_telefone = Label(self.frame_1,text="Telefone",bg='#F5F5DC')
        self.lb_codigo_telefone.place(relx=0.45,rely=0.67,relheight=0.09,relwidth=0.075)

        self.codigo_entry_telefone = Entry(self.frame_1)
        self.codigo_entry_telefone.place(relx=0.45,rely=0.79,relheight=0.1,relwidth=0.25)

        self.mensagem = Label(self.frame_1,text="",bg="#003366",fg="white")
        self.mensagem.place(relx=0.1, rely=0.0, relwidth=0.2, relheight=0.10)

    def objetos_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_1, height=3, columns=('col1', 'col2', 'col3', 'col4','col5'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='ID')
        self.listaCli.heading('#2', text='Modelo Carro')
        self.listaCli.heading('#3', text='Transmissão')
        self.listaCli.heading('#4', text='Motor')
        self.listaCli.heading('#5',text='Combustivel')

        self.listaCli.column('#0',width=1)
        self.listaCli.column('#1',width=50)
        self.listaCli.column('#2',width=50)
        self.listaCli.column('#3',width=100)
        self.listaCli.column('#4',width=125)
        self.listaCli.column('#5',width=125)

        self.listaCli.place(relx=0.1, rely=0.9, relheight=0.6, relwidth=0.7)

        self.scrollista = Scrollbar(self.frame_1,orient='vertical')
        self.listaCli.configure(yscrollcommand=self.scrollista.set)
        self.scrollista.place(relx=0.80,rely=0.9,relheight=0.77,relwidth=0.03)


aplicacao = Aplicacao

