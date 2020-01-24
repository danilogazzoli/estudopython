class Movimentacao:
    """ Classe para movimentação da conta corrente"""
    def __init__(self, valor):
        self.operacao = 0
        self.valor = 0

class Saque(Movimentacao):
    """ Classe para saques """
    def __init__(self, valor):
        super().__init__(valor)
        self.valor = valor
        self.operacao = -1

class Deposito(Movimentacao):
    """ Classe para saques """
    def __init__(self, valor):
        super().__init__(valor)
        self.valor = valor
        self.operacao = 1
