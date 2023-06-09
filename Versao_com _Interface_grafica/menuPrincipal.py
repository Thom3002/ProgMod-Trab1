import tkinter as tk

class InterfaceCliente(tk.Tk):
    def botao_alugar_jogo_clicked(self):
        print("Botão 'Alugar Jogo' clicado")

    def botao_retornar_jogo_clicked(self):
        print("Botão 'Retornar Jogo' clicado")
    
    def botao_voltar_clicked(self):
        self.destroy()  # Fecha a janela
        menu_principal = MenuPrincipal()
        menu_principal.mainloop()

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Interface do Cliente")

        container = tk.Frame(self)
        container.pack(expand=True, padx=20, pady=20)

        container.columnconfigure(0, weight=1)
        container.rowconfigure([0, 1, 2], weight=1)

        titulo = tk.Label(
            container,
            text="Bem-vindo, Cliente!\nSelecione uma opção:",
            font=("Arial", 16),
        )
        titulo.grid(row=0, column=0, pady=40)

        botao_alugar_jogo = tk.Button(
            container, text="Alugar Jogo", command=self.botao_alugar_jogo_clicked
        )
        botao_retornar_jogo = tk.Button(
            container, text="Retornar Jogo", command=self.botao_retornar_jogo_clicked
        )
        botao_voltar = tk.Button(
            container, text="Voltar", command=self.botao_voltar_clicked
        )

        botao_alugar_jogo.grid(row=1, column=0, sticky="nsew", pady=10)
        botao_retornar_jogo.grid(row=2, column=0, sticky="nsew", pady=10)
        botao_voltar.grid(row=3, column=0, sticky="nsew", pady=10)


class InterfaceLocadora(tk.Tk):
    def botao_cadastrar_clicked(self):
        print("Botão 'Cadastrar novo cliente' clicado")

    def botao_visualizar_clicked(self):
        print("Botão 'Consultar estoque' clicado")

    def botao_alterar_clicked(self):
        print("Botão 'Alterar dados' clicado")

    def botao_adicionar_clicked(self):
        print("Botão 'Adicionar/Excluir jogo' clicado")

    def botao_transacoes_clicked(self):
        print("Botão 'Transações' clicado")

    def botao_aluguel_clicked(self):
        print("Botão 'Registro de aluguel' clicado")
    
    def botao_voltar_clicked(self):
        self.destroy()  # Fecha a janela
        menu_principal = MenuPrincipal()
        menu_principal.mainloop()

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Interface da Locadora")

        container = tk.Frame(self)
        container.pack(expand=True, padx=20, pady=20)

        container.columnconfigure(0, weight=1)
        container.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)

        titulo = tk.Label(
            container,
            text="Bem-vindo, Locadora!\nSelecione uma opção:",
            font=("Arial", 16),
        )
        titulo.grid(row=0, column=0, pady=40)

        botao_cadastrar = tk.Button(
            container, text="Cadastrar novo cliente", command=self.botao_cadastrar_clicked
        )
        botao_visualizar = tk.Button(
            container, text="Consultar estoque", command=self.botao_visualizar_clicked
        )
        botao_alterar = tk.Button(
            container, text="Alterar dados", command=self.botao_alterar_clicked
        )
        botao_adicionar = tk.Button(
            container, text="Adicionar/Excluir jogo", command=self.botao_adicionar_clicked
        )
        botao_transacoes = tk.Button(
            container, text="Transações", command=self.botao_transacoes_clicked
        )
        botao_aluguel = tk.Button(
            container, text="Registro de aluguel", command=self.botao_aluguel_clicked
        )
        botao_voltar = tk.Button(
            container, text="Voltar", command=self.botao_voltar_clicked
        )

        botao_cadastrar.grid(row=1, column=0, sticky="nsew", pady=10)
        botao_visualizar.grid(row=2, column=0, sticky="nsew", pady=10)
        botao_alterar.grid(row=3, column=0, sticky="nsew", pady=10)
        botao_adicionar.grid(row=4, column=0, sticky="nsew", pady=10)
        botao_transacoes.grid(row=5, column=0, sticky="nsew", pady=10)
        botao_aluguel.grid(row=6, column=0, sticky="nsew", pady=10)
        botao_voltar.grid(row=7, column=0, sticky="nsew", pady=10)


class MenuPrincipal(tk.Tk):
    def botao_cliente_clicked(self):
        self.destroy()  # Fecha a janela
        self.result = 1
        interface_cliente = InterfaceCliente()
        interface_cliente.mainloop()

    def botao_locadora_clicked(self):
        self.destroy()  # Fecha a janela
        self.result = 2
        interface_locadora = InterfaceLocadora()
        interface_locadora.mainloop()

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Menu Principal")

        container = tk.Frame(self)
        container.pack(expand=True, padx=20, pady=20)

        container.columnconfigure(0, weight=1)
        container.rowconfigure([0, 1, 2, 3], weight=1)

        titulo = tk.Label(
            container,
            text="Bem-vindo!\nSelecione a opção desejada.",
            font=("Arial", 16),
        )
        titulo.grid(row=0, column=0, pady=40)

        botao_cliente = tk.Button(
            container, text="Cliente", command=self.botao_cliente_clicked
        )
        botao_locadora = tk.Button(
            container, text="Locadora", command=self.botao_locadora_clicked
        )

        botao_cliente.grid(row=1, column=0, sticky="nsew", pady=10)
        botao_locadora.grid(row=2, column=0, sticky="nsew", pady=10)
        
        
    def run(self):
        self.mainloop()





    
