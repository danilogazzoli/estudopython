class Correntista:
    def __init__(self, nome, cpf, saldo_inicial):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo_inicial

    def nome(self):
        return self.__nome

    def cpf(self):
        return self.__cpf

    def saldo(self):
        return self.__saldo

    def deposita(self, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor deve ser float")

        if valor <= 0.0:
            raise ValueError(f"Valor '{valor}' não permitido para deposito")

        self.__saldo += valor

    def saque(self, valor):
        if not isinstance(valor, float):
            raise TypeError("Valor deve ser float")

        if valor <= 0.0:
            raise ValueError(f"Valor '{valor}' não permitido para saque")

        if valor > self.__saldo:
            raise ValueError(f"Saldo insuficiente para saque no valor de '{valor}'")

        self.__saldo -= valor