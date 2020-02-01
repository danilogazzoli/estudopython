from cpf import Cpf
from correntista import Correntista
from excecoes import ListaVazia

class Banco:
    """ Deve implmentar o cadastro de novos correntistas
        Deve implementar a procura de correnstias por nome
        Deve implementar a listagem de todos os correntistas """

    def __init__(self):
        self.__listac = []

    def print_correntistas(self, lista):    
        for c in lista:
            print('Código: {}, Nome: {}, CPF: {}, Saldo: {}'.format(c.codigo, c.nome, c.Cpf.strcpf, c.saldo))

    def display_correntistas(self):
        if len(self.__listac) == 0:
            raise ListaVazia 
        self.print_correntistas(__listac)
    
    @property
    def get_correntistas_count(self):
        cont = len(self.__listac)
        print('passou aqui {}'.format(cont))
        return int(cont)

    def cadastra_correntista(self, correntista):
        self.__listac.append(correntista)
        
    def find_correntista_por_codigo(self, codigo):
        correntista = None
        for c in self.__listac:
            if c.codigo == codigo:
                correntista = c
                break
        return correntista

    def find_correntista_por_nome(self, nome):
        retorno = []
        for c in self.__listac:
            if nome in c.nome:
                retorno.append(c)
        self.print_correntistas(retorno)
        return retorno

