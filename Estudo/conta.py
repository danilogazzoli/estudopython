class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def deposita(self, valor):
        self.saldo += valor
    def saca(self, valor):
        self.saldo -= valor
    def extrato(self):
        print('Número: {} \nSaldo: {}'.format(self.numero, self.saldo))

conta = Conta('1234', 'Aparecida', 120, 1000)
conta.deposita(100)
conta.extrato()
conta.saca(50)
conta.extrato()
print(conta.__dir__())