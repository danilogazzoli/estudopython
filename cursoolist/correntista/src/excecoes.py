class SaldoNegativo(Exception):
    """ Classe para saldo negativo """
    pass

class OpcaoInvalida(Exception):
    """ Classe para opção inválida de input no menu """
    pass

class ListaVazia(Exception):
    """ Classe para quando a lista de correntistas estiver vazia """
    pass

class CpfInvalido(Exception):
    """ Classe para quando o cpf estiver inválido """
    pass
