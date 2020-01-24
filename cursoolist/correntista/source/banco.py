from cpf import Cpf
from correntista import Correntista
from excecoes import ListaVazia

class Banco:
    """ Deve implmentar o cadastro de novos correntistas
        Deve implementar a procura de correnstias por nome
        Deve implementar a listagem de todos os correntistas """

    def __init__(self):
        self.__listac = []

    def printCorrentistas(self, lista):    
        for c in lista:
            print('Código: {}, Nome: {}, CPF: {}, Saldo: {}'.format(c.codigo, c.nome, c.Cpf.strcpf, c.saldo))

    def displayCorrentistas(self):
        if len(self.__listac) == 0:
            raise ListaVazia 
        self.printCorrentistas(__listac)

    def cadastrarCorrentista(self):
        print('Digite o nome:') 
        nome = input()
        print('Saldo inicial:')
        saldoinicial = int(input())
        print('CPF:')
        cpf = input()
        cp = Cpf(cpf)
        c = Correntista(len(self.__listac) + 1,  nome, cp, saldoinicial)
        self.__listac.append(c)
        
    def findCorrentistaPorCodigo(self, codigo):
        correntista = None
        for c in self.__listac:
            if c.codigo == codigo:
                correntista = c
                break
        return correntista

    def findCorrentistaPorNome(self, nome):
        retorno = []
        for c in self.__listac:
            if nome in c.nome:
                retorno.append(c)
        self.printCorrentistas(retorno)
        return retorno

