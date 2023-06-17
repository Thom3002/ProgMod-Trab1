# -*- coding: utf-8 -*-
import os
import platform
import sys
from time import sleep
import json

TEMPO_CARREGAMENTO = 1.5
LOGIN_FEITO = False
lista_clientes = []
lista_jogos = []
global nome_cliente 


# Definição de funções

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


def exibir_menu_principal():  # MENU PRINCIPAL
    clear()
    exibir_jogos(lista_jogos)
    print("__________________________")
    print("MENU PRINCIPAL\n")
    print("1 - Cliente")
    print("2 - Locadora")

    print("\n0 - Encerrar programa")

    print("__________________________\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_menu_cliente()
    elif opcao == "2":
        exibir_menu_locadora()
    elif opcao == "0":
        animacao_espera(TEMPO_CARREGAMENTO, "ENCERRANDO PROGRAMA...")
        if lista_jogos:
            registra_json(lista_jogos, "estoque.json")
        if lista_clientes:
            registra_json(lista_clientes, "clientes.json")    
        sys.exit()
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
        exibir_menu_principal()


def exibir_menu_cliente():  # MENU CLIENTE
    global lista_clientes
    global lista_jogos
    global LOGIN_FEITO
    clear()
    
    if LOGIN_FEITO:
        print(f"Olá {nome_cliente}. Seja bem vindo à locadora!")
        print()
        print("__________________________")
        print("MENU CLIENTE\n")
        print("1 - Alugar jogo")
        print("2 - Retornar jogo")
        print("3 - Voltar")
        print("\n\n4 - Logout")
        print("__________________________\n")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alugar_jogo()
        elif opcao == "2":
            retornar_jogo()
        elif opcao == "3":  # Voltar
            clear()
            animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
            exibir_menu_principal()
        elif opcao == "4": # Logout
            LOGIN_FEITO = False
            clear()
            print("Logout selecionado.\n")
            animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
            exibir_menu_principal()
        else:
            print("\nOpção inválida! Tente novamente.\n")
            animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
            exibir_menu_cliente()
        continua("cliente")
        
    else:
        if valida_cliente(lista_clientes) == False:
            print("Cliente não cadastrado. Favor faça seu cadastro: \n")
            lista_clientes = cadastrar_cliente(lista_clientes)
            continua("cliente")
        else:
            animacao_espera(TEMPO_CARREGAMENTO, "LOGIN REALIZADO COM SUCESSO! REDIRECIONANDO PARA O MENU CLIENTE...")
            LOGIN_FEITO = True
            exibir_menu_cliente()
            

def exibir_menu_locadora():  # MENU LOCADORA
    clear()
    global lista_jogos
    global lista_clientes

    print("Estoque atual:")
    print(lista_jogos)
    print("__________________________")
    print("MENU LOCADORA\n")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar jogo")
    print("3 - Excluir jogo")
    print("4 - Consultar estoque")
    print("5 - Transações")
    print("6 - Registro de Aluguel")
    print("7 - Alterar dados")
    print("8 - Exibir clientes")
    print("9 - Voltar")
    print("__________________________\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clear()
        lista_clientes = cadastrar_cliente(lista_clientes)
    elif opcao == "2":
        lista_jogos = cadastrar_jogo(lista_jogos)
        print("Lista jogos apos a chamada da função cadastrar jogo")
        print(lista_jogos)
        
    elif opcao == "3":
        excluir_jogo(lista_jogos)
    elif opcao == "4":
        consultar_estoque(lista_jogos)
    elif opcao == "5":
        transacoes()
    elif opcao == "6":
        registro_aluguel()
    elif opcao == "7":
        alterar_dados()
    elif opcao == "8":
        exibir_clientes(lista_clientes)
    elif opcao == "9":  # Voltar
        clear()
        animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
        exibir_menu_principal()

    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
        exibir_menu_locadora()
        
    continua("locadora") #volta para o menu locadora


# FUNCOES CLIENTE
def alugar_jogo(lista_jogos, lista_clientes):
    clear()
    print("Opção 'Alugar jogo' selecionada.\n")
    exibir_jogos(lista_jogos)


def retornar_jogo():
    clear()
    print("Opção 'Retornar jogo' selecionada.\n")
  
def valida_cliente(lista_clientes): # verifica se o cliente existe no cadastro tipo um login
    global nome_cliente
    clear()
    nome_cliente = input("LOGIN\nPara continuar, digite seu nome: ")
    for cliente in lista_clientes:
        if cliente['nome'] == nome_cliente:
            return True
    return False

# FUNCOES LOCADORA
def cadastrar_cliente(lista_clientes):
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    email = input("Digite o e-mail do cliente: ")

    clientes = {'nome': nome, 'cpf': cpf, 'email': email}
    lista_clientes.append(clientes)
    print("Cliente cadastrado com sucesso!")
    # print(lista_clientes)
    return lista_clientes


def cadastrar_jogo(lista_jogos):
    print("Opção 'Cadastrar jogo' selecionada.\n")
    clear()
    jogo_id = input("Digite o id do jogo: ")
    nome = input("Digite o nome do jogo: ")
    qtd = input("Numero de unidades: ")
    preco_aluguel = input("Preço de aluguel(diária): R$ ")
    jogo = {'jogo_id': jogo_id, 'nome': nome, 'qtd': qtd, 'preco_aluguel': preco_aluguel}
    lista_jogos.append(jogo)
    # print(lista_jogos)
    return lista_jogos


def excluir_jogo(lista_jogos):
    clear()
    print("Opção 'Excluir jogo' selecionada.\n")
    if not lista_jogos:
        print("A lista de jogos está vazia.")
    else:
        exibir_jogos(lista_jogos)

        jogo_id = input("\nDigite o ID do jogo que você deseja excluir: ")

        for jogo in lista_jogos:
            if jogo['jogo_id'] == jogo_id:
                lista_jogos.remove(jogo)
                print("Jogo removido com sucesso!")
                break
        else:
            print("Jogo não encontrado!")

        exibir_jogos(lista_jogos)


def exibir_jogos(lista_jogos):  # Auxiliar para excluir jogos
    if not lista_jogos:
        print("A lista de jogos está vazia.")
    else:
        print("Jogos disponíveis:")
        i = 1
        for jogo in lista_jogos:
            print(f"{i}. ID: {jogo['jogo_id']} | Nome: {jogo['nome']} | Quantidade: {jogo['qtd']} | Preço de aluguel(diária): R$ {jogo['preco_aluguel']}")
            i += 1

def exibir_clientes(lista_clientes):  
    clear()
    print("Opção 'Exibir clientes' selecionada.\n")
    if not lista_clientes:
        print("A lista de clientes está vazia.")
    else:
        print("Lista de clientes cadastrados:")
        i = 1
        for cliente in lista_clientes:
            print(f"{i}. Nome: {cliente['nome']} | CPF: {cliente['cpf']} | E-mail: {cliente['email']}")
            i += 1
                        
def consultar_estoque(jogos):
    global lista_clientes
    clear()
    print("Opção 'Consultar estoque' selecionada.\n")
    if not jogos:
        print("Estoque vazio.")
    else:
        exibir_jogos(jogos)


def transacoes():
    clear()
    print("Opção 'Transações' selecionada.\n")


def registro_aluguel():
    clear()
    print("Opção 'Registro de Aluguel' selecionada.\n")


def alterar_dados():
    clear()
    print("Opção 'Alterar dados' selecionada.\n")


# OUTRAS FUNÇOES
def animacao_espera(segundos, mensagem):
    animacao = "|/-\\"
    i = 0
    while segundos > 0:
        print(mensagem, animacao[i % len(animacao)], end="\r")
        i += 1
        sleep(0.1)
        segundos -= 0.1
    clear()


def continua(menu):
    print("\nDeseja continuar?\n")
    print("1 - SIM")
    print("2 - NAO")
    print("__________________________\n")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":  # SIM
        if menu == "cliente":
            exibir_menu_cliente()
        else:
            exibir_menu_locadora()
    elif opcao == "2":  # NAO
        animacao_espera(TEMPO_CARREGAMENTO, "ENCERRANDO PROGRAMA...")
        if lista_jogos:
            registra_json(lista_jogos, "estoque.json")
        if lista_clientes:
            registra_json(lista_clientes, "clientes.json")
        sys.exit()
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
        continua(menu)


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# main
lista_jogos = ler_json("estoque.json")
lista_clientes = ler_json("clientes.json")
exibir_menu_principal()

