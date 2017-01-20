import MySQLdb
import sys


class Banco:

    def __init__(self, host, user, passwd, db):
        self.con = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.cursor = self.con.cursor()

    """

    Consultas às tabelas

    """

    # Consultar clientes pelo nome
    def consultaClienteNome(self, nomeCliente):
        self.cursor.execute("SELECT * FROM Cliente WHERE nomeCli = '%s'" % str(nomeCliente))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar clientes pelo CPF
    def consultaClienteCPF(self, cpfCliente):
        self.cursor.execute("SELECT * FROM Cliente WHERE cpf = '%s'" % str(cpfCliente))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todos os clientes cadastrados
    def consultaClientes(self):
        self.cursor.execute("SELECT * FROM Cliente")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo modelo
    def consultaComputadorModelo(self, modelo):
        self.cursor.execute("SELECT * FROM Computador WHERE modelo = '%s'" % str(modelo))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo número de série
    def consultaComputadorNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Computador WHERE numSerie = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar computador pelo cpf do cliente
    def consultaComputadorCliente(self, cpfCli):
        self.cursor.execute("SELECT * FROM Computador WHERE cpfCli = '%s'" % str(cpfCli))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todos os computadores cadastrados
    def consultaComputadores(self):
        self.cursor.execute("SELECT * FROM Computador")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peça pelo código
    def consultaPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca WHERE codPeca = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar todas as peças
    def consultaPecas(self):
        self.cursor.execute("SELECT * FROM Peca")
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pelo número de série do computador
    def consultaServicoPecaNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE numSerieMaquina = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pelo código da peça
    def consultaServicoPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE codPecaServico = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar peças que estão sendo utilizadas em algum serviço pela data programada
    def consultaServicoPecaData(self, dataProgramada):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE dataProgramadaServico = '%s'" % str(dataProgramada))
        resultado = self.cursor.fetchall()
        print(resultado)

    # Consultar serviço de upgrade pelo número de série do computador
    def consultaServicoNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM manutencao.Upgrade_Revisao WHERE numSerieComputador = '%s';" % str(numSerie))
        resultado = self.cursor.fetchall()
        print(resultado)

    """

    Metodos de inserção nas tabelas

    """

    # Cadastrar Cliente
    def CadastrarCliente(self, cpf, nomeCli):
        self.cursor.execute("INSERT INTO `manutencao`.`Cliente` (`cpf`, `nomeCli`) VALUES ('"+str(cpf)+"', '"+str(nomeCli)+"');")
        self.con.commit()

    # Cadastrar Computador
    def CadastrarComputador(self, numSerie, modelo, cpfCli):
        try:
            self.cursor.execute("INSERT INTO `manutencao`.`Computador` (`numSerie`, `modelo`, `cpfCli`) VALUES ('"+str(numSerie)+"', '"+str(modelo)+"', '"+str(cpfCli)+"');")
            self.con.commit()
        except MySQLdb.IntegrityError:
            print("Erro de integridade:", sys.exc_info()[1])
        except:
            print("Erro inesperado:", sys.exc_info())
    
    # Cadastrar Peca
    def CadastrarAluguelRelacionamento(self, codPeca,descricao):
        self.cursor.execute("INSERT INTO `manutencao`.`Peca` (`codPeca`, `descricao`) VALUES ('"+str(codPeca)+"','"+str(descricao)+"');")
        self.con.commit()
    
    # Cadastrar relação Peca com Upgrade Revisao
    def CadastrarPecaUpgradeRevisao(self, numSerieMaquina,dataProgramadaServico,codPecaServico,quantidade):
        self.cursor.execute("INSERT INTO `manutencao`.`Peca_Upgrade_Revisao` (`numSerieMaquina`,`dataProgramadaServico`,`codPecaServico`,`quantidade`) VALUES ('"+str(numSerieMaquina)+"', '"+str(dataProgramadaServico)+"', '"+str(codPecaServico)+"', '"+str(quantidade)+"');")
        self.con.commit()

    #Cadastrar Upgrade Revisao
    def CadastrarUpgradeRevisao(self, numSerieComputador,dataProgramada,dataUltimoUpgrade,dataExecutada):
        self.cursor.execute("INSERT INTO `manutencao`.`Upgrade_Revisao` (`numSerieComputador`,`dataProgramada`,`dataUltimoUpgrade`,`dataExecutada`) VALUES ('"+str(numSerieComputador)+"', '"+str(dataProgramada)+"', '"+str(dataUltimoUpgrade)+"', '"+str(dataExecutada)+"');")
        self.con.commit()

    """

    Métodos de remoção nas tabelas

    """

    # Remover Cliente utilizando o CPF
    def removerCliente(self, cpfCli):
        self.cursor.execute("DELETE FROM `manutencao`.`Cliente` WHERE cpf = '%s';" % str(cpfCli))
        self.con.commit()

    # Remover Computador utilizando o CPF do cliente e o Número de série do Computador
    def removerComputadorCliente(self, cpfCli, numSerie):
        self.cursor.execute("DELETE FROM `manutencao`.`Computador` WHERE cpfCli = '%s' AND numSerie = '%s';" % (str(cpfCli), str(numSerie)))
        self.con.commit()

    # Remover Peça utilizando o Código da peça
    def removerPeca(self, codPeca):
        self.cursor.execute("DELETE FROM `manutencao`.`Peca` WHERE codPeca = '%s';" % str(codPeca))
        self.con.commit()

    # Remover serviço de upgrade de peça utilizando o Número de série do Computador e o Código da peça
    def removerPecaUpgrade(self, numSerie, codPeca):
        self.cursor.execute("DELETE FROM `manutencao`.`Peca_Upgrade_Revisao` WHERE numSerieMaquina = '%s' AND codPecaServico = '%s';" % (str(numSerie), str(codPeca)))
        self.con.commit()

    # Remover serviço de upgrade utilizando o Número de série do computador
    def removerUpgrade(self, numSerie):
        self.cursor.execute("DELETE FROM `manutencao`.`Upgrade_Revisao` WHERE numSerieComputador = '%s';" % str(numSerie))
        self.con.commit()

"""

Código para testar os métodos - Apagar para versão final

"""

bd = Banco('localhost', 'root', 'root', 'manutencao')
#bd.CadastrarCliente(123, "Daniel")
bd.consultaClienteCPF(123)
bd.CadastrarComputador("123ABC", "MAX123", 123)
#bd.CadastrarComputador("ABC123", "MAX123", 123)
bd.consultaComputadorCliente(123)
#bd.removerComputadorCliente(123, "123ABC")
#bd.consultaComputadorCliente(123)
#bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, " ")
bd.consultaServicoNumSerie("ABC123")

