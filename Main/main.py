import MySQLdb
from Banco.banco import Banco
import sys, os

cabecalho = "########### Manutenção de Computadores DCJV Ltda. ###########\n"

def mainMenu():
    os.system('clear')

    print(cabecalho)
    print("Escolha uma das opções a seguir:\n")
    print("1. Cadastro")
    print("2. Consulta")
    print("3. Remoção")
    print("4. Edição")
    print("0. Sair")

    escolha = input(">> ")
    exec_menu(escolha)

    return

def exec_menu(escolha):
    os.system('clear')
    opcao = escolha.lower()
    print(opcao)
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['main_menu']()

    return

def cadastro():
    print(cabecalho)
    print("########### Cadastro ###########\n")
    print("1. Cadastrar cliente")
    print("2. Cadastrar máquina")
    print("3. Cadastrar peça")
    print("4. Cadastrar serviço")
    print("5. Cadastrar peça em serviço")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    if(escolha == '1'):
        cpf = input("Informe o CPF do cliente: ")
        nome = input("Informe o Nome do cliente: ")
        try:
            bd.CadastrarCliente(cpf, nome)
            print("Cliente cadastrado com sucesso!")
            menu_actions['1']()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
            menu_actions['1']()
        except:
            print("Erro inesperado:", sys.exc_info())
            menu_actions['main_menu']()

    elif(escolha == '2'):
        numSerie = input("Informe o Número de série da máquina: ")
        modelo = input("Informe o Modelo da máquina: ")
        cpfCli = input("Informe o CPF do cliente: ")
        try:
            bd.CadastrarComputador(numSerie, modelo, cpfCli)
            print("Máquina cadastrada com sucesso!")
            menu_actions['1']()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
            menu_actions['1']()
        except:
            print("Erro inesperado:", sys.exc_info())
            menu_actions['main_menu']()

    elif(escolha == '3'):
        codPeca = input("Informe o Código da peça: ")
        descricao = input("Informe uma descrição da peça: ")
        try:
            bd.CadastrarPeca(codPeca, descricao)
            print("Peça cadastrada com sucesso!")
            menu_actions['1']()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
            menu_actions['1']()
        except:
            print("Erro inesperado:", sys.exc_info())
            menu_actions['main_menu']()

    elif(escolha == '4'):
        numSerieComputador = input("Informe o Número de série da máquina: ")
        dataProgramada = input("Informe a Data programada: ")
        try:
            bd.CadastrarUpgradeRevisao(numSerieComputador, dataProgramada)
            print("Serviço cadastrado com sucesso!")
            menu_actions['1']()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
            menu_actions['1']()
        except:
            print("Erro inesperado:", sys.exc_info())
            menu_actions['main_menu']()

    elif(escolha == '5'):
        numSerieMaquina = input("Informe o Número de série da máquina: ")
        dataProgramadaServico = input("Informe a data programada do serviço: ")
        codPecaServico = input("Informe o Código da peça: ")
        quantidade = input("Informe a Quantidade: ")
        try:
            bd.CadastrarPecaUpgradeRevisao(numSerieMaquina, dataProgramadaServico, codPecaServico, quantidade)
            print("Serviço de peça cadastrado com sucesso!")
            menu_actions['1']()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
            menu_actions['1']()
        except:
            print("Erro inesperado:", sys.exc_info())
            menu_actions['main_menu']()

    elif(escolha == '9'):
        back()

    elif(escolha == '0'):
        exit()

    return



def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()

menu_actions = {
    'main_menu': mainMenu,
    '1': cadastro,
    '9': back,
    '0': exit
}

if __name__ == "__main__":
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    mainMenu()

# bd = Banco('localhost', 'root', 'root', 'manutencao')
# bd.CadastrarCliente(123, "Daniel")
# bd.consultaClienteCPF(123)
# bd.CadastrarComputador("123ABC", "MAX123", 123)
#
# # bd.CadastrarComputador("ABC123", "MAX123", 123)
# bd.consultaComputadorCliente(123)
# # bd.removerComputadorCliente(123, "123ABC")
# # bd.consultaComputadorCliente(123)
# # bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, " ")
#
# #bd.CadastrarComputador("ABC123", "MAX123", 123)
# bd.consultaComputadorCliente(123)
# #bd.removerComputadorCliente(123, "123ABC")
# #bd.consultaComputadorCliente(123)
# #bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, " ")
#
# bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, "")
# bd.consultaServicoNumSerie("ABC123")
# bd.removerComputadorCliente(123, "ABC123")
# bd.removerCliente(123)
