class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number

class Conta:
    def __init__(self, numero,titular, saldo, limite):
        '''
        este é o construtor da classe e este é um comentário
        de várias linhas
        '''

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    def deposita(self, valor):
        self.__saldo += valor
    def saca(self, valor):
        self.__saldo -= valor
    def extrato(self):
        print('Número: {} \nSaldo: {}'.format(self.__numero, self.__saldo))
    @property 
    def numero(self):
        return self.__numero 
    @numero.setter
    def numero(self, numero):
        self.__numero = numero



conta = Conta('2323','Aparecida', 120, 1000)
conta.numero = '1234'
conta.deposita(100)
conta.extrato()
conta.saca(50)
conta.extrato()
conta.numero = '456'
conta.extrato()
print(conta.__dir__())