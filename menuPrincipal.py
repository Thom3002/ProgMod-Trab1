import tkinter as tk


class JanelaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("Menu Principal")

        container = tk.Frame(self)
        container.pack(expand=True, padx=20, pady=20)

        container.columnconfigure(0, weight=1)
        container.rowconfigure([0, 1, 2, 3], weight=1)

        # Adicionando o título
        titulo = tk.Label(
            container,
            text="Bem vindo!\nSelecione a opção desejada.",
            font=("Arial", 16),
        )
        titulo.grid(row=0, column=0, pady=40)

        botao_cliente = tk.Button(container, text="Cliente")
        botao_locadora = tk.Button(container, text="Locadora")
        # botao_deletar = tk.Button(container, text="Excluir jogo")

        botao_cliente.grid(row=1, column=0, sticky="nsew", pady=10)
        botao_locadora.grid(row=2, column=0, sticky="nsew", pady=10)
        # botao_deletar.grid(row=4, column=0, sticky="nsew", pady=10)


if __name__ == "__main__":
    janela = JanelaPrincipal()
    janela.mainloop()
