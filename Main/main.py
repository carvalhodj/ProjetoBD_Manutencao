from Banco.banco import Banco

bd = Banco('localhost', 'root', 'root', 'manutencao')
bd.CadastrarCliente(123, "Daniel")
bd.consultaClienteCPF(123)
bd.CadastrarComputador("123ABC", "MAX123", 123)

# bd.CadastrarComputador("ABC123", "MAX123", 123)
bd.consultaComputadorCliente(123)
# bd.removerComputadorCliente(123, "123ABC")
# bd.consultaComputadorCliente(123)
# bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, " ")

#bd.CadastrarComputador("ABC123", "MAX123", 123)
bd.consultaComputadorCliente(123)
#bd.removerComputadorCliente(123, "123ABC")
#bd.consultaComputadorCliente(123)
#bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, " ")

bd.CadastrarUpgradeRevisao("ABC123", 20170101, 20160102, "")
bd.consultaServicoNumSerie("ABC123")
bd.removerComputadorCliente(123, "ABC123")
bd.removerCliente(123)
