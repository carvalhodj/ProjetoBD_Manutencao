import MySQLdb

class Banco:

    def __init__(self, host, user, passwd, db):
        con = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
        self.cursor = con.cursor()

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


"""

Código para testar os métodos - Apagar para versão final

"""

bd = Banco('localhost', 'root', 'root', 'manutencao')
bd.consultaClienteNome('Pedro')
bd.consultaClienteCPF(12345678998)
bd.consultaClientes()
bd.consultaComputadorCliente(12345678998)
bd.consultaComputadores()