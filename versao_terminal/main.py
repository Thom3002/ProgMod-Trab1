import os
import platform
import sys
from time import *

TEMPO_CARREGAMENTO = 1.5

 #definição de funcoes
 
def exibir_menu_principal(): # MENU PRINCIPAL
    clear()
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
        sys.exit()
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
        exibir_menu_principal()


def exibir_menu_cliente(): # MENU CLIENTE
    clear()
    
    print("__________________________") 
    print("MENU CLIENTE\n")
    print("1 - Alugar jogo")
    print("2 - Retornar jogo")
    print("3 - Voltar")
    print("__________________________\n") 
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        alugar_jogo()
    elif opcao == "2":
        retornar_jogo()
    elif opcao == "3": #Voltar
        clear()
        animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
        exibir_menu_principal()
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
        exibir_menu_cliente()
    continua("cliente") 

def exibir_menu_locadora(): # MENU LOCADORA
    clear()
    
    print("__________________________") 
    print("MENU LOCADORA\n")
    print("1 - Cadastrar cliente")
    print("2 - Consultar estoque")
    print("3 - Alterar dados")
    print("4 - Adicionar/excluir jogo")
    print("5 - Transações")
    print("6 - Registro de Aluguel")
    print("7 - Voltar")
    print("__________________________\n") 
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        consultar_estoque()
    elif opcao == "3":
        alterar_dados()
    elif opcao == "4":
        adicionar_excluir_jogo()
    elif opcao == "5":
        transacoes()
    elif opcao == "6":
        registro_aluguel()
    elif opcao == "7": #Voltar
        clear()
        animacao_espera(TEMPO_CARREGAMENTO, "REDIRECIONANDO PARA MENU PRINCIPAL")
        exibir_menu_principal()
     
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
        exibir_menu_locadora()
        
    continua("locadora")       

# FUNCOES CLIENTE
def alugar_jogo():
    clear()
    print("Opção 'Alugar jogo' selecionada.")
def retornar_jogo():
    clear()
    print("Opção 'Retornar jogo' selecionada.")

# FUNCOES LOCADORA
def cadastrar_cliente():
    clear()
    print("Opção 'Cadastrar cliente' selecionada.")

def consultar_estoque():
    clear()
    print("Opção 'Consultar estoque' selecionada.")

def alterar_dados():
    clear()
    print("Opção 'Alterar dados' selecionada.")

def adicionar_excluir_jogo():
    clear()
    print("Opção 'Adicionar/excluir jogo' selecionada.")

def transacoes():
    clear()
    print("Opção 'Transações' selecionada.")

def registro_aluguel():
    clear()
    print("Opção 'Registro de Aluguel' selecionada.")

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
    
    if opcao == "1": # SIM
        if menu == "cliente":
            exibir_menu_cliente()
        else:
            exibir_menu_locadora()    
    elif opcao == "2": # NAO
        animacao_espera(TEMPO_CARREGAMENTO, "ENCERRANDO PROGRAMA...")
        sys.exit(0)
    else:
        print("\nOpção inválida! Tente novamente.\n")
        animacao_espera(TEMPO_CARREGAMENTO, "Aguarde um momento...")
        continua(menu)
    
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
        
#main
exibir_menu_principal()

