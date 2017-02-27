import MySQLdb
from Banco.banco import Banco
import sys, os

cabecalho = "########### Manutenção de Computadores DCJV Ltda. ###########\n"

"""

Menus

"""

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

    exec_menu_cadastro(escolha)

    return

def consulta():
    print(cabecalho)
    print("########### Consulta ###########\n")
    print("1. Consultar cliente")
    print("2. Consultar máquina")
    print("3. Consultar peça")
    print("4. Consultar serviço")
    print("5. Consultar peça em serviço")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta(escolha)

    return

def consultaCliente():
    print(cabecalho)
    print("########### Consulta - Cliente ###########\n")
    print("1. Consultar cliente pelo nome")
    print("2. Consultar cliente pelo CPF")
    print("3. Consultar todos os clientes")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta_cliente(escolha)

    return

def consultaMaquina():
    print(cabecalho)
    print("########### Consulta - Máquina ###########\n")
    print("1. Consultar máquina pelo Modelo")
    print("2. Consultar máquina pelo Número de série")
    print("3. Consultar máquina pelo CPF do cliente")
    print("4. Consultar máquina pelo CPF do cliente e Número de série")
    print("5. Consultar todas as máquinas")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta_maquina(escolha)

    return

def consultaPeca():
    print(cabecalho)
    print("########### Consulta - Peça ###########\n")
    print("1. Consultar peça pelo código")
    print("2. Consultar todas as peças")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta_peca(escolha)

    return

def consultaServico():
    print(cabecalho)
    print("########### Consulta - Serviço ###########\n")
    print("1. Consultar serviço pelo Número de série da máquina")
    print("2. Consultar serviço pela data programada")
    print("3. Consultar serviço pela data executada")
    print("4. Consultar todos os serviços")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta_servico(escolha)

    return

def consultaPecaServico():
    print(cabecalho)
    print("########### Consulta - Peças em serviço ###########\n")
    print("1. Consultar peças em serviço pelo Número de série da máquina")
    print("2. Consultar peças em serviço pelo código da peça")
    print("3. Consultar peças em serviço pela data programada")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_consulta_peca_servico(escolha)

    return

def remocao():
    print(cabecalho)
    print("########### Remoção ###########\n")
    print("1. Remover cliente")
    print("2. Remover máquina")
    print("3. Remover serviço")
    print("4. Remover peça")
    print("5. Remover peça em serviço")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_remocao(escolha)

    return

def edicao():
    print(cabecalho)
    print("########### Edição ###########\n")
    print("1. Editar cliente")
    print("2. Editar máquina")
    print("3. Editar serviço")
    print("4. Editar peça")
    print("5. Editar peça em serviço")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_edicao(escolha)

    return

def editarCliente():
    print(cabecalho)
    print("########### Edição - Cliente ###########\n")
    print("1. Editar nome do cliente")
    print("9. Voltar")
    print("0. Sair")

    escolha = input(">> ")

    exec_menu_edicao_cliente(escolha)

    return

def editarMaquina():
    return  # TODO

def editarPeca():
    return  # TODO

def editarServico():
    return  # TODO

def editarPecaServico():
    return  # TODO

"""

Execução das escolhas

"""

def exec_menu(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['main_menu']()

    return

def exec_menu_cadastro(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_cadastro[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['1']()

    return

def exec_menu_consulta(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['2']()

    return

def exec_menu_consulta_cliente(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta_cliente[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_consulta['1']()

    return

def exec_menu_consulta_maquina(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta_maquina[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_consulta['2']()

    return

def exec_menu_consulta_peca(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta_peca[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_consulta['3']()

    return

def exec_menu_consulta_servico(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta_servico[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_consulta['4']()

    return

def exec_menu_consulta_peca_servico(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_consulta_peca_servico[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_consulta['5']()

    return

def exec_menu_remocao(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_remocao[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['main_menu']()

    return

def exec_menu_edicao(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_edicao[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_actions['main_menu']()

    return

def exec_menu_edicao_cliente(escolha):
    os.system('clear')
    opcao = escolha.lower()
    if(opcao == ''):
        menu_actions['main_menu']()
    else:
        try:
            menu_edicao_cliente[opcao]()
        except KeyError:
            print("Opção inválida. Tente novamente.")
            menu_edicao['1']()

    return
"""

Funções

"""

def cadastrarCliente():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    cpf = input("Informe o CPF do cliente: ")
    nome = input("Informe o Nome do cliente: ")
    try:
        bd.CadastrarCliente(cpf, nome)
        print("Cliente cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def cadastrarMaquina():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    numSerie = input("Informe o Número de série da máquina: ")
    modelo = input("Informe o Modelo da máquina: ")
    cpfCli = input("Informe o CPF do cliente: ")
    try:
        bd.CadastrarComputador(numSerie, modelo, cpfCli)
        print("Máquina cadastrada com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def cadastrarPeca():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    codPeca = input("Informe o Código da peça: ")
    descricao = input("Informe uma descrição da peça: ")
    try:
        bd.CadastrarPeca(codPeca, descricao)
        print("Peça cadastrada com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def cadastrarServico():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    numSerieComputador = input("Informe o Número de série da máquina: ")
    dataProgramada = input("Informe a Data programada: ")
    try:
        bd.CadastrarUpgradeRevisao(numSerieComputador, dataProgramada)
        print("Serviço cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def cadastrarPecaServico():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    numSerieMaquina = input("Informe o Número de série da máquina: ")
    dataProgramadaServico = input("Informe a data programada do serviço: ")
    codPecaServico = input("Informe o Código da peça: ")
    quantidade = input("Informe a Quantidade: ")
    try:
        bd.CadastrarPecaUpgradeRevisao(numSerieMaquina, dataProgramadaServico, codPecaServico, quantidade)
        print("Serviço de peça cadastrado com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['1']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def consultaClienteNome():
    nome = input("Digite o nome do cliente: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaClienteNome(nome)
    print(("Nome: %s\nCPF: %s\n") % (resultado[0][0], resultado[0][1]))
    input("Pressione ENTER para continuar...")
    menu_consulta['1']()

def consultaClienteCPF():
    cpf = input("Digite o CPF do cliente: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaClienteCPF(cpf)
    print("Nome: %s\nCPF: %s\n" % (resultado[0][0], resultado[0][1]))
    input("Pressione ENTER para continuar...")
    menu_consulta['1']()

def consultaClientes():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaClientes()
    for cliente in resultado:
        print("Nome: %s\nCPF: %s\n" % (cliente[0], cliente[1]))
    input("Pressione ENTER para continuar...")
    menu_consulta['1']()

def consultaMaquinaModelo():
    modelo = input("Digite o modelo da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaComputadorModelo(modelo)
    for maquina in resultado:
        print("Num. Série: %s\nModelo: %s\nCPF: %s\n" % (maquina[0], maquina[1], maquina[2]))
    input("Pressione ENTER para continuar...")
    menu_consulta['2']()

def consultaMaquinaNumSerie():
    numSerie = input("Digite o Número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaComputadorNumSerie(numSerie)
    print("Num. Série: %s\nModelo: %s\nCPF: %s\n" % (resultado[0][0], resultado[0][1], resultado[0][2]))
    input("Pressione ENTER para continuar...")
    menu_consulta['2']()

def consultaMaquinaCPFCliente():
    cpf = input("Digite o CPF do cliente: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaComputadorCliente(cpf)
    for maquina in resultado:
        print("Num. Série: %s\nModelo: %s\nCPF: %s\n" % (maquina[0], maquina[1], maquina[2]))
    input("Pressione ENTER para continuar...")
    menu_consulta['2']()

def consultaMaquinaCPFClienteNumSerie():
    cpf = input("Digite o CPF do cliente: ")
    numSerie = input("Digite o Número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaComputadorClienteCpfNumSerie(cpf, numSerie)
    print("Num. Série: %s\nModelo: %s\nCPF: %s\n" % (resultado[0][0], resultado[0][1],resultado[0][2]))
    input("Pressione ENTER para continuar...")
    menu_consulta['2']()

def consultaComputadores():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaComputadores()
    for maquina in resultado:
        print("Num. Série: %s\nModelo: %s\nCPF: %s\n" % (maquina[0], maquina[1], maquina[2]))
    input("Pressione ENTER para continuar...")
    menu_consulta['2']()

def consultaPecaCod():
    codPeca = input("Digite o código da peça: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaPecaCod(codPeca)
    print("Código: %s\nDescrição: %s\n" % (resultado[0][0], resultado[0][1]))
    input("Pressione ENTER para continuar...")
    menu_consulta['3']()

def consultaPecas():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaPecas()
    for peca in resultado:
        print("Código: %s\nDescrição: %s\n" % (peca[0], peca[1]))
    input("Pressione ENTER para continuar...")
    menu_consulta['3']()

def consultaServicoNumSerie():
    numSerie = input("Digite o Número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoNumSerie(numSerie)
    print("Número de série da maquina:%s\nData programada:%s\nData do ultimo Upgrade:%s\nData Executada:%s\n" % (resultado[0][0],resultado[0][1],resultado[0][2],resultado[0][3]))
    input("Pressione ENTER para continuar...")
    menu_consulta['4']()

def consultaServicoDataProg():
    dataProg = input("Digite a data programada do serviço (Formato: AAAAMMDD) : ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoDataProg(dataProg)
    print("Número de série da maquina:%s\nData programada:%s\nData do ultimo Upgrade:%s\nData Executada:%s\n" % (resultado[0][0], resultado[0][1], resultado[0][2], resultado[0][3]))
    input("Pressione ENTER para continuar...")
    menu_consulta['4']()

def consultaServicoDataExec():
    dataExec = input("Digite a data executada do serviço (Formato: AAAAMMDD) : ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoDataExec(dataExec)
    print("Número de série da maquina:%s\nData programada:%s\nData do ultimo Upgrade:%s\nData Executada:%s\n" % (resultado[0][0],resultado[0][1], resultado[0][2], resultado[0][3]))
    input("Pressione ENTER para continuar...")
    menu_consulta['4']()

def consultaServicos():
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultarServicos()
    for servico in resultado:
        print("Número de série da maquina:%s\nData programada:%s\nData do ultimo Upgrade:%s\nData Executada:%s\n" % (servico[0],servico[1], servico[2], servico[3]))
    input("Pressione ENTER para continuar...")
    menu_consulta['4']()

def consultaServicoPecaNumSerie():
    numSerie = input("Digite o Número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoPecaNumSerie(numSerie)
    peca=bd.consultaPecaCod(resultado[0][2])
    print("Número de série da maquina:%s\nData programada:%s\nPeca:%s\nQuantidade:%s\n" %(resultado[0][0],resultado[0][1],peca[0][1],resultado[0][3]) )
    input("Pressione ENTER para continuar...")
    menu_consulta['5']()

def consultaServicoPecaCod():
    codPeca = input("Digite o código da peça: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoPecaCod(codPeca)
    print(resultado)
    input("Pressione ENTER para continuar...")
    menu_consulta['5']()

def consultaServicoPecaData():
    dataProg = input("Digite a data programada do serviço (Formato: AAAAMMDD) : ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    resultado = bd.consultaServicoPecaData(dataProg)
    print(resultado)
    input("Pressione ENTER para continuar...")
    menu_consulta['5']()

def removerCliente():
    cpfCli = input("Digite o CPF do cliente a remover: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.removerCliente(cpfCli)
        print("Cliente removido com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['3']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def removerComputadorCliente():
    cpfCli = input("Digite o CPF do cliente dono da máquina: ")
    numSerie = input("Digite o número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.removerComputadorCliente(cpfCli, numSerie)
        print("Máquina removida com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['3']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def removerUpgrade():
    numSerie = input("Digite o número de série da máquina: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.removerUpgrade(numSerie)
        print("Serviço removido com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['3']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def removerPeca():
    codPeca = input("Digite o código da peça: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.removerPeca(codPeca)
        print("Peça removida com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['3']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def removerPecaUpgrade():
    numSerie = input("Digite o número de série da máquina: ")
    codPeca = input("Digite o código da peça: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.removerPecaUpgrade(numSerie, codPeca)
        print("Peça removida do serviço com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['3']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()

def editarNomeCliente():
    cpfCliente = input("Digite o CPF do cliente a alterar o nome: ")
    nomeCliente = input("Digite o novo nome do cliente: ")
    bd = Banco('localhost', 'root', 'root', 'manutencao')
    try:
        bd.editarClienteNome(cpfCliente, nomeCliente)
        print("Nome do cliente alterado com sucesso!")
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    except MySQLdb.IntegrityError:
        print("Erro de integridade:", sys.exc_info()[1])
        input("Pressione ENTER para continuar...")
        menu_actions['4']()
    except:
        print("Erro inesperado:", sys.exc_info())
        input("Pressione ENTER para continuar...")
        menu_actions['main_menu']()
    return




def back():
    menu_actions['main_menu']()

def exit():
    sys.exit()

"""

Listas das funções

"""

menu_actions = {
    'main_menu': mainMenu,
    '1': cadastro,
    '2': consulta,
    '3': remocao,
    '4': edicao,
    '9': back,
    '0': exit
}

menu_cadastro = {
    '1': cadastrarCliente,
    '2': cadastrarMaquina,
    '3': cadastrarPeca,
    '4': cadastrarServico,
    '5': cadastrarPecaServico,
    '9': back,
    '0': exit
}

menu_consulta = {
    '1': consultaCliente,
    '2': consultaMaquina,
    '3': consultaPeca,
    '4': consultaServico,
    '5': consultaPecaServico,
    '9': back,
    '0': exit
}

menu_consulta_cliente = {
    '1': consultaClienteNome,
    '2': consultaClienteCPF,
    '3': consultaClientes,
    '9': back,
    '0': exit
}

menu_consulta_maquina = {
    '1': consultaMaquinaModelo,
    '2': consultaMaquinaNumSerie,
    '3': consultaMaquinaCPFCliente,
    '4': consultaMaquinaCPFClienteNumSerie,
    '5': consultaComputadores,
    '9': back,
    '0': exit
}

menu_consulta_peca = {
    '1': consultaPecaCod,
    '2': consultaPecas,
    '9': back,
    '0': exit
}

menu_consulta_servico = {
    '1': consultaServicoNumSerie,
    '2': consultaServicoDataProg,
    '3': consultaServicoDataExec,
    '4': consultaServicos,
    '9': back,
    '0': exit
}

menu_consulta_peca_servico = {
    '1': consultaServicoPecaNumSerie,
    '2': consultaServicoPecaCod,
    '3': consultaServicoPecaData,
    '9': back,
    '0': exit
}

menu_remocao = {
    '1': removerCliente,
    '2': removerComputadorCliente,
    '3': removerUpgrade,
    '4': removerPeca,
    '5': removerPecaUpgrade,
    '9': back,
    '0': exit
}

menu_edicao = {
    '1': editarCliente,
    '2': editarMaquina,
    '3': editarServico,
    '4': editarPeca,
    '5': editarPecaServico,
    '9': back,
    '0': exit
}

menu_edicao_cliente = {
    '1': editarNomeCliente,
    '9': back,
    '0': exit
}

if __name__ == "__main__":
    mainMenu()
