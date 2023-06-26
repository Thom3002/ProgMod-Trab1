import os
import platform
from time import sleep
import json
import sys

# Variáveis globais
TEMPO_CARREGAMENTO = 1 # tempo da animacao de carregamento
LOGIN_FEITO = False
CONTADOR = 0 # Conta quantas vezes um jogo que está sem estoque foi solicitado, se chegar a 3 dispara ao fornecedor a solicitação do jogo
REPOSICAO_QTD = 6 # Quantidade de jogos solicitados ao fornecedor quando acaba o estoque 


saldo = 0
lista_clientes = []
lista_jogos = []

def registra_pedidos(nome_jogo, quantidade): # auxiliar para funcao alugar_jogo() dentro do modulo cliente
    pedido = {"nome": nome_jogo, "qtd": quantidade}
    
    # Verifica se o arquivo já existe
    try:
        with open('pedidos.json', 'r') as arquivo:
            lista_pedidos = json.load(arquivo)
    except FileNotFoundError:
        lista_pedidos = []
    
    # Adiciona o novo pedido à lista
    lista_pedidos.append(pedido)
    
    with open('pedidos.json', 'w') as arquivo:
        json.dump(lista_pedidos, arquivo, ensure_ascii=False, indent=4)

def ler_resposta_json(lista_jogos, saldo):
    encontrou = False
    msgLog = []
    
    with open('resposta.json', 'r') as file:
        data = json.load(file)
    
    for jogo_resposta in data:
        if jogo_resposta['aprovado'] == 1:
            animacao_espera(TEMPO_CARREGAMENTO + 2, "Processando resposta do fornecedor para o jogo: {}, do arquivo de resposta do fornecedor...".format(jogo_resposta["nome"]))
            
            if saldo >= jogo_resposta['preco']:
                for jogo_lista in lista_jogos:
                    if jogo_lista["nome"] == jogo_resposta["nome"]:
                        encontrou = True
                        jogo_lista["qtd"] += REPOSICAO_QTD
                        novo_saldo = saldo - jogo_resposta["preco"]
                        msgLog.append("Reposição de estoque do jogo: {} realizada com sucesso!\nNovo saldo: (R$ {} - R$ {}) = R$ {}".format(jogo_lista["nome"], saldo, jogo_resposta["preco"], novo_saldo))
                        saldo = novo_saldo
                
                if not encontrou:
                    msgLog.append("ERRO 001: {} não está cadastrado no estoque da locadora.".format(jogo_resposta["nome"]))
            else:
                msgLog.append("Saldo insuficiente para comprar o jogo: {}. Preço do jogo: R$ {} | Saldo: R$ {}".format(jogo_resposta["nome"], jogo_resposta["preco"], saldo))
        else: # jogo não aprovado
            animacao_espera(TEMPO_CARREGAMENTO + 1, "Processando resposta do fornecedor para o jogo: {}, do arquivo de resposta do fornecedor...".format(jogo_resposta["nome"]))
            msgLog.append("Fornecedor não possui estoque do jogo: {}. Reposição em andamento...".format(jogo_resposta["nome"]))
            for jogo_lista in lista_jogos:
                if jogo_lista["nome"] == jogo_resposta["nome"]:
                    encontrou = True
                    jogo_lista["cont"] = 2 # proxima vez que alguem tentar alugar o jogo, solicitara um novo pedido ao fornecedor
            if not encontrou:
                msgLog.append("ERRO 002: {} não está cadastrado no estoque da locadora.".format(jogo_resposta["nome"]))
    
    with open('resposta.json', 'w') as file_w:
        file_w.write('')
    
    print("Conteúdo do arquivo resposta.json foi apagado.\n_______________________________")
    print("Atualizações: ")
    for msg in msgLog:
        print(msg)
    print("_______________________________\n")
    return lista_jogos, saldo


def fornecedor_respondeu(): # verifica se json está vazio
    if os.path.getsize('resposta.json') > 0:
        return True
    else:
        return False


def exibir_jogos(lista_jogos):  # Auxiliar para excluir jogos
    if not lista_jogos:
        print("A lista de jogos está vazia.")
    else:
        print("Jogos disponíveis:")
        i = 1
        for jogo in lista_jogos:
            print(f"{str(i).ljust(3)} | ID: {str(jogo['jogo_id']).ljust(4)} | Nome: {jogo['nome'].ljust(20)} | Quantidade: {str(jogo['qtd']).ljust(4)} | Preço de aluguel(diária): R$ {str(jogo['preco_aluguel']).ljust(5)}")

            i += 1


def animacao_espera(segundos, mensagem):
    animacao = "|/-\\"
    i = 0
    while segundos > 0:
        print(mensagem, animacao[i % len(animacao)], end="\r")
        i += 1
        sleep(0.1)
        segundos -= 0.1
    clear()


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        