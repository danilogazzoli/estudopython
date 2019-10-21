class Conta(object): # (object) não necessário
    def __init__(self, numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.total = saldo * limite

    def deposita(self, valor):
        self.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    @property
    def titular(self):
        return self.__titular

    @numero.setter
    def numero(self, valor):
        self.__titular = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    def extrato(self):
        print('Saldo é %s'%(self.__saldo))

class ContaCorrente(Conta):
    def __init__(self,  numero, titular, saldo, limite, dv):
        super().__init__(numero, titular, saldo, limite)
        self.__dv = dv

    def extrato(self):
        super().extrato()
        #print('Conta %s dv %s'%(super().numero, self.__dv))
        print('Conta %s dv %s' % (self._Conta__numero, self.__dv))



if __name__ == '__main__':
    conta = Conta('123-4', 'João', 1000)
    print('Número: %s \nTitular: %s \nSaldo: %s' %(conta.numero, conta.titular, conta.saldo))
    conta.deposita(50.0)
    print(vars(conta))

    cc = ContaCorrente('200', 'Maria', 1000, 10000, 5)
    cc.extrato()
    print(vars(cc)) # visualizar os atributos
    print(id(cc)) # visualizar o endereço do objeto
    print(int(id(cc)))