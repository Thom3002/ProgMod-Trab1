import tkinter as tk


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Menu Locadora")

        container = tk.Frame(self)
        container.pack(expand=True, padx=20, pady=20)

        container.columnconfigure(0, weight=2)
        container.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=1)

        # Adicionando o título
        titulo = tk.Label(
            container,
            text="Bem vindo ao menu locadora!\nSelecione a opção desejada.",
            font=("Arial", 16),
        )
        titulo.grid(row=0, column=0, pady=40, sticky="N", columnspan=2)

        botao_cadastrar = tk.Button(container, text="Cadastrar novo cliente")
        botao_visualizar = tk.Button(container, text="Consultar estoque")
        botao_alterar = tk.Button(container, text="Alterar dados")
        botao_adicionar = tk.Button(container, text="Adicionar/Excluir jogo")
        botao_transacoes = tk.Button(container, text="Transações")
        botao_aluguel = tk.Button(container, text="Registro de aluguel")
        # botao_deletar = tk.Button(container, text="Excluir jogo")

        botao_cadastrar.grid(row=1, column=0, sticky="nsew", pady=5)
        botao_visualizar.grid(row=2, column=0, sticky="nsew", pady=5)
        botao_alterar.grid(row=3, column=0, sticky="nsew", pady=5)
        botao_adicionar.grid(row=4, column=0, sticky="nsew", pady=5)
        botao_transacoes.grid(row=5, column=0, sticky="nsew", pady=5)
        botao_aluguel.grid(row=6, column=0, sticky="nsew", pady=5)
        # botao_deletar.grid(row=4, column=0, sticky="nsew", pady=10)


if __name__ == "__main__":
    janela = JanelaPrincipal()
    janela.mainloop()
