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
        self.cursor.close()
        return resultado

    # Consultar clientes pelo CPF
    def consultaClienteCPF(self, cpfCliente):
        self.cursor.execute("SELECT * FROM Cliente WHERE cpf = '%s'" % str(cpfCliente))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar todos os clientes cadastrados
    def consultaClientes(self):
        self.cursor.execute("SELECT * FROM Cliente")
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    ###
    # Consultar computador pelo modelo
    def consultaComputadorModelo(self, modelo):
        self.cursor.execute("SELECT * FROM Computador WHERE modelo = '%s'" % str(modelo))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar computador pelo número de série
    def consultaComputadorNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Computador WHERE numSerie = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar computador pelo cpf do cliente
    def consultaComputadorCliente(self, cpfCli):
        self.cursor.execute("SELECT * FROM Computador WHERE cpfCli = '%s'" % str(cpfCli))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar computador pelo cpf do cliente e número de série do computador
    def consultaComputadorClienteCpfNumSerie(self, cpfCli, numSerie):
        self.cursor.execute("SELECT * FROM Computador WHERE cpfCli = '%s' AND numSerie = '%s'" % (str(cpfCli), str(numSerie)))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar todos os computadores cadastrados
    def consultaComputadores(self):
        self.cursor.execute("SELECT * FROM Computador")
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    ###
    # Consultar peça pelo código
    def consultaPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca WHERE codPeca = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar todas as peças
    def consultaPecas(self):
        self.cursor.execute("SELECT * FROM Peca")
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    ###
    # Consultar peças que estão sendo utilizadas em algum serviço pelo número de série do computador
    def consultaServicoPecaNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE numSerieMaquina = '%s'" % str(numSerie))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        self.con.close()
        return resultado

    # Consultar peças que estão sendo utilizadas em algum serviço pelo código da peça
    def consultaServicoPecaCod(self, codPeca):
        self.cursor.execute("SELECT * FROM Peca_Upgrade_Revisao WHERE codPecaServico = '%s'" % str(codPeca))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    # Consultar peças que estão sendo utilizadas em algum serviço pela data programada
    def consultaServicoPecaData(self, dataProgramada):
        self.cursor.execute(
            "SELECT * FROM Peca_Upgrade_Revisao WHERE dataProgramadaServico = '%s'" % str(dataProgramada))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    ###
    # Consultar serviço de upgrade pelo número de série do computador
    def consultaServicoNumSerie(self, numSerie):
        self.cursor.execute("SELECT * FROM manutencao.Upgrade_Revisao WHERE numSerieComputador = '%s';" % str(numSerie))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    def consultaServicoDataProg(self, dataProg):
        self.cursor.execute("SELECT * FROM `manutencao`.`Upgrade_Revisao` WHERE dataProgramada = '%s';" % str(dataProg))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    def consultaServicoDataExec(self, dataExec):
        self.cursor.execute("SELECT * FROM `manutencao`.`Upgrade_Revisao` WHERE dataExecutada = '%s';" % str(dataExec))
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    def consultarServicos(self):
        self.cursor.execute("SELECT * FROM manutencao.Upgrade_Revisao;")
        resultado = self.cursor.fetchall()
        self.cursor.close()
        return resultado

    """

    Metodos de inserção nas tabelas

    """

    # Cadastrar Cliente
    def CadastrarCliente(self, cpf, nomeCli):
        self.cursor.execute("INSERT INTO `manutencao`.`Cliente` (`cpf`, `nomeCli`) VALUES ('"+str(cpf)+"', '"+str(nomeCli)+"');")
        self.con.commit()
        self.cursor.close()

    # Cadastrar Computador
    def CadastrarComputador(self, numSerie, modelo, cpfCli):
        self.cursor.execute("INSERT INTO `manutencao`.`Computador` (`numSerie`, `modelo`, `cpfCli`) VALUES ('"+str(numSerie)+"', '"+str(modelo)+"', '"+str(cpfCli)+"');")
        self.con.commit()
        self.cursor.close()

    # Cadastrar Peca
    def CadastrarPeca(self, codPeca,descricao):
        self.cursor.execute("INSERT INTO `manutencao`.`Peca` (`codPeca`, `descricao`) VALUES ('"+str(codPeca)+"','"+str(descricao)+"');")
        self.con.commit()
        self.cursor.close()

    # Cadastrar relação Peca com Upgrade Revisao
    def CadastrarPecaUpgradeRevisao(self, numSerieMaquina,dataProgramadaServico,codPecaServico,quantidade):
        self.cursor.execute("INSERT INTO `manutencao`.`Peca_Upgrade_Revisao` (`numSerieMaquina`,`dataProgramadaServico`,`codPecaServico`,`quantidade`) VALUES ('"+str(numSerieMaquina)+"', '"+str(dataProgramadaServico)+"', '"+str(codPecaServico)+"', '"+str(quantidade)+"');")
        self.con.commit()
        self.cursor.close()

    #Cadastrar Upgrade Revisao
    def CadastrarUpgradeRevisao(self, numSerieComputador,dataProgramada):
        self.cursor.execute("INSERT INTO `manutencao`.`Upgrade_Revisao` (`numSerieComputador`,`dataUltimoUpgrade`) VALUES ('"+str(numSerieComputador)+"', '"+str(dataProgramada)+"');")
        self.con.commit()
        self.cursor.close()


    """

    Métodos de remoção nas tabelas

    """

    # Remover Cliente utilizando o CPF
    def removerCliente(self, cpfCli):
        self.cursor.execute("DELETE FROM `manutencao`.`Cliente` WHERE cpf = '%s';" % str(cpfCli))
        self.con.commit()
        self.cursor.close()

    # Remover Computador utilizando o CPF do cliente e o Número de série do Computador
    def removerComputadorCliente(self, cpfCli, numSerie):
        self.cursor.execute("DELETE FROM `manutencao`.`Computador` WHERE cpfCli = '%s' AND numSerie = '%s';" % (str(cpfCli), str(numSerie)))
        self.con.commit()
        self.cursor.close()
        self.con.close()

    # Remover Peça utilizando o Código da peça
    def removerPeca(self, codPeca):
        self.cursor.execute("DELETE FROM `manutencao`.`Peca` WHERE codPeca = '%s';" % str(codPeca))
        self.con.commit()
        self.cursor.close()

    # Remover serviço de upgrade de peça utilizando o Número de série do Computador e o Código da peça
    def removerPecaUpgrade(self, numSerie, codPeca):
        self.cursor.execute("DELETE FROM `manutencao`.`Peca_Upgrade_Revisao` WHERE numSerieMaquina = '%s' AND codPecaServico = '%s';" % (str(numSerie), str(codPeca)))
        self.con.commit()
        self.cursor.close()

    # Remover serviço de upgrade utilizando o Número de série do computador
    def removerUpgrade(self, numSerie):
        self.cursor.execute("DELETE FROM `manutencao`.`Upgrade_Revisao` WHERE numSerieComputador = '%s';" % str(numSerie))
        self.con.commit()
        self.cursor.close()
            
    """
    
    Métodos de Edição
    
    """

    # Editar nome dos clientes pelo cpf
    def editarClienteNome(self, cpfCliente, novoNome):
        self.cursor.execute("UPDATE `manutencao`.`Cliente` SET `nomeCli` = '%s' WHERE `cpf` = '%s';" % (str(novoNome), str(cpfCliente)))
        self.con.commit()
        self.cursor.close()

    # Editar descricao da peca pelo codigo
    def editarPecaDescricao(self, codPeca, novaDescricao):
        self.cursor.execute("UPDATE `manutencao`.`Peca` SET `descricao`="+str(novaDescricao)+" WHERE `codPeca`="+str(codPeca)+";")
        self.con.commit()
        self.cursor.close()

    # Editar data executada
    def editarUpgrade_RevisaoDataExecutada(self,numSerieComputador,dataExecutada):
        self.cursor.execute("UPDATE `manutencao`.`Upgrade_Revisao` SET `dataExecutada`="+str(dataExecutada)+" WHERE `numSerieComputador`="+str(numSerieComputador)+";")
        self.con.commit()
        self.cursor.close()

    #Editar data programada
    def editarUpgrade_RevisaoDataProgramada(self, numSerieComputador, dataProgramada):
        self.cursor.execute("UPDATE `manutencao`.`Upgrade_Revisao` SET `dataProgramada`=" + str(dataProgramada) + " WHERE `numSerieComputador`=" + str(numSerieComputador) + ";")
        self.con.commit()
        self.cursor.close()
         

    #Editar modelo do  computador
    def editarComputadorModelo(self, numSerie,novoModelo):
        self.cursor.execute("UPDATE `manutencao`.`Computador` SET `modelo`= "+str(novoModelo)+" WHERE `numSerie`="+str(numSerie)+";")
        self.con.commit()
        self.cursor.close()

    #Editar dono do  computador
    def editarComputadorDono(self, numSerie,cpfCli):
        self.cursor.execute("UPDATE `manutencao`.`Computador` SET `cpfCli`="+str(cpfCli)+" WHERE `numSerie`="+str(numSerie)+";")
        self.con.commit()
        self.cursor.close()

    #Editar quantidade na relacao peca e upgrade
    def editarQuantidadePecaUpgrade(self, numSerieMaquina,dataProgramadaServico,codPecaServico, novaQuantidade):
        self.cursor.execute("UPDATE `manutencao`.`Peca_Upgrade_Revisao` SET `quantidade`="+str(novaQuantidade)+" WHERE `numSerieMaquina`="+str(numSerieMaquina)+" and`dataProgramadaServico`="+str(dataProgramadaServico)+" and`codPecaServico`="+str(codPecaServico)+";")
        self.con.commit()
        self.cursor.close()

banco=Banco('localhost', 'root', 'root', 'manutencao')
print(banco.consultaComputadorClienteCpfNumSerie(123456789,"3233jjd213"))
