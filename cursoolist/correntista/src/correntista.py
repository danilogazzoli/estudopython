from movimentacao import Saque, Deposito
from cpf import Cpf
from excecoes import SaldoNegativo
from auditoriaCorrentistas import AuditoriaCorrentistas


class Correntista:
    """ Classe correntista """
    def __init__(self, codigo, nome, Cpf, saldoinicial):
        self.codigo = codigo
        self.nome = nome
        self.saldo = 0
        self.Cpf = Cpf
        self.historico = []
        self.deposita(saldoinicial)
        self.auditoria = AuditoriaCorrentistas()
        self.auditoria.get_instance().adicionar_registros(self.Cpf, self.historico)

    def deposita(self, valor):
        """ Método para depósito """
        dep = Deposito(valor)
        self.incrementa_saldo(dep) 

    def saque(self, valor):
        """ método para saque """    
        saq = Saque(valor)
        self.incrementa_saldo(saq) 
    
    def incrementa_saldo(self,movimentacao):
        """ Método para incrementar"""
        self.saldo = self.saldo + (movimentacao.valor * movimentacao.operacao) 
        if self.saldo < 0:
            self.saldo = self.saldo + movimentacao.valor
            raise SaldoNegativo 
        self.historico.append(movimentacao)

    def serialize(self):
        return {
            'nome': self.nome,
            'cpf': self.Cpf.strcpf,
            'saldo': self.saldo}    

    def __next__(self):
        if self.indice >= len(self.historico):
            raise StopIteration
        else:
            hist = self.historico[self.indice]
            self.indice += 1
        return hist

    def __iter__(self):
       """ Retorna o objeto iterável """
       self.indice = 0
       return self
