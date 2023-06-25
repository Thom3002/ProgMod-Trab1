import os
import platform
import sys
from time import sleep
import json

# Variáveis globais
TEMPO_CARREGAMENTO = 1 # tempo da animacao de carregamento
LOGIN_FEITO = False
CONTADOR = 0 # Conta quantas vezes um jogo que está sem estoque foi solicitado, se chegar a 3 dispara ao fornecedor a solicitação do jogo
REPOSICAO_QTD = 6 # Quantidade de jogos solicitados ao fornecedor quando acaba o estoque

lista_clientes = []
lista_jogos = [] 

global nome_cliente
global saldo

# Definição de funções

#FUNCOES DA MAIN DE LEITURA E ESCRITA DE ARQUIVOS
def registra_json(lista, nome_arquivo):  # Escreve a lista no arquivo json 
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

def ler_json(nome_arquivo): # le o json e retorna-o como uma lista
    if os.path.isfile(nome_arquivo):  # Verifica se o arquivo existe
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = json.load(arquivo)
                return conteudo
        except json.decoder.JSONDecodeError:
            print(f"O arquivo {nome_arquivo} está vazio ou possui uma formatação inválida.")
            return []
    else:
        print(f"O arquivo {nome_arquivo} não existe.")
        sys.exit()

def ler_saldo_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo:
        linha = arquivo.readline()
        saldo_str = linha.split('R$ ')[1].strip()
        saldo = int(saldo_str)
        return saldo
    
def registra_saldo_arquivo(saldo):
    with open('caixa.txt', 'r+') as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if linha.startswith('Saldo: R$'):
                linhas[i] = 'Saldo: R$ ' + str(saldo) + '\n'
                break
        arquivo.seek(0)
        arquivo.writelines(linhas)
        arquivo.truncate()

def registra_pedidos(nome_jogo, quantidade):
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


# FUNCOES CLIENTE
def alugar_jogo(lista_jogos, nome_jogo):
    global saldo
    encontrou = False
    for jogo in lista_jogos:
        if jogo["nome"] == nome_jogo:
            #print("\n__________________________\n")
            encontrou = True
            opcao_valida = False
            if jogo["qtd"] > 0:
              print("Jogo alugado com sucesso")
            else:
                jogo["cont"] += 1
                print("Sem estoque. {}° solicitação.".format(jogo["cont"]))
                if jogo["cont"] == 3:
                    print("Mandando reposicao de estoque do jogo {} ao fornecedor.".format(jogo["nome"]))
                    registra_pedidos(jogo["nome"], REPOSICAO_QTD)
                    jogo["cont"] = 0
            break
    if not encontrou:
        print("Jogo não encontrado no estoque.")
   
def retornar_jogo(nome_jogo):
    global lista_jogos
    encontrou = False
    #clear()
    #print("Opção 'Retornar jogo' selecionada.\n")
    #exibir_jogos(lista_jogos)
    #print("__________________________\n")
    #nome_jogo = input("Digite o nome do jogo a ser retornado: ")
    for jogo in lista_jogos:
        if jogo["nome"] == nome_jogo:
            encontrou = True
            print("\nJogo retornado com sucesso!")
            jogo["qtd"] += 1 
            print("{}:  | Quantidade no estoque atualizada: {}\n".format(nome_jogo, jogo["qtd"]))
            break
    if not encontrou:
        print("Jogo não encontrado no estoque.")

def valida_cliente(lista_clientes, nome_cliente):
    for cliente in lista_clientes:
        if cliente['nome'] == nome_cliente:
            print("Cliente já cadastrado.")
            return True
    print("Cliente não cadastrado")
    return False

# FUNCOES LOCADORA
def cadastrar_cliente(lista_clientes, nome, cpf, email):
  if (valida_cliente(lista_clientes, nome) == False):
    clientes = {'nome': nome, 'cpf': cpf, 'email': email}
    lista_clientes.append(clientes)
    print("Cliente cadastrado com sucesso!")
    # print(lista_clientes)
    return lista_clientes


def cadastrar_jogo(lista_jogos, jogo_id, nome, qtd, preco_aluguel):
  if jogo_id == '' or nome == '' or qtd == 0 or preco_aluguel == 0:
    print("Não foi possível cadastrar esse jogo")
  else:
    jogo = {'jogo_id': jogo_id, 'nome': nome, 'qtd': qtd, 'preco_aluguel': preco_aluguel, 'cont': 0}
    lista_jogos.append(jogo)
    print("Jogo cadastrado com sucesso")
    return lista_jogos

def excluir_jogo(lista_jogos, jogo_id):
  if not lista_jogos:
    print("A lista de jogos está vazia.")
  else:
    for jogo in lista_jogos:
      if jogo['jogo_id'] == jogo_id:
        lista_jogos.remove(jogo)
        print("Jogo removido com sucesso!")
        break
    else:
      print("Jogo não encontrado no estoque.")

def exibir_jogos(lista_jogos): 
    if lista_jogos == []:
        print("A lista de jogos está vazia.")
    else:
        print("Jogos disponíveis:")
        i = 1
        for jogo in lista_jogos:
            print(f"{str(i).ljust(3)} | ID: {str(jogo['jogo_id']).ljust(4)} | Nome: {jogo['nome'].ljust(20)} | Quantidade: {str(jogo['qtd']).ljust(4)} | Preço de aluguel(diária): R$ {str(jogo['preco_aluguel']).ljust(5)}")

            i += 1

def exibir_clientes(lista_clientes):  
    if lista_clientes == []:
        print("A lista de clientes está vazia.")
    else:
        print("Lista de clientes cadastrados:")
        i = 1
        for cliente in lista_clientes:
            print(f"{str(i).ljust(3)} | Nome: {cliente['nome'].ljust(25)} | CPF: {cliente['cpf'].ljust(14)} | E-mail: {cliente['email']}")

            i += 1
                        
def consultar_estoque(jogos):
    global lista_clientes
    # clear()
    print("Opção 'Consultar estoque' selecionada.\n")
    if not jogos:
        print("Estoque vazio.")
    else:
        exibir_jogos(jogos)


# lendo arquivos
lista_jogos = ler_json("estoque.json")
lista_clientes = ler_json("clientes.json")
saldo = ler_saldo_arquivo("caixa.txt")
lista_vazia = []

# TESTES

# funções cliente

print("FUNÇÃO DE ALUGAR JOGO:")
print('')
alugar_jogo(lista_jogos, 'Banco Imobiliário')
print('')
alugar_jogo(lista_jogos, 'Detetive')
print('')
alugar_jogo(lista_jogos, 'Detetive')
print('')
alugar_jogo(lista_jogos, 'Detetive')

print("\n__________________________\n")
print("FUNÇÃO DE RETORNAR JOGO:")
retornar_jogo('Banco Imobiliário')
retornar_jogo('Monopoly')

print("\n__________________________\n")
print("FUNÇÃO DE VALIDAR CLIENTE:")
print('')
valida_cliente(lista_clientes, "Natalia")
print('')
valida_cliente(lista_clientes, "Thomas")

# funções locadora

print("\n__________________________\n")
print("FUNÇÃO DE CADASTRAR CLIENTE:")
print('')
cadastrar_cliente(lista_clientes, "Natalia", '06410614713', 'natalia.grossmann@hotmail.com')
print('')
cadastrar_cliente(lista_clientes, "Thomas", 'bcbbc', 'hshs')

print("\n__________________________\n")
print("FUNÇÃO DE CADASTRAR JOGOS:")
print('')
cadastrar_jogo(lista_jogos, '5', 'Monopoly', 3, 5)
print('')
cadastrar_jogo(lista_jogos, '5', 'Monopoly', 3, 0)

print("\n__________________________\n")
print("FUNÇÃO DE EXCLUIR JOGOS:")
print('')
excluir_jogo(lista_jogos, '1')
print('')
excluir_jogo(lista_jogos, '40')

print("\n__________________________\n")
print("FUNÇÃO DE EXIBIR JOGOS:")
print('')
exibir_jogos(lista_jogos)
print('')
exibir_jogos(lista_vazia)

print("\n__________________________\n")
print("FUNÇÃO DE EXIBIR CLIENTES:")
print('')
exibir_clientes(lista_clientes)
print('')
exibir_clientes(lista_vazia)
