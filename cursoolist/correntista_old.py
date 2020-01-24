import os
clear = lambda: os.system('clear')

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

class Cpf:
    "classe para validação de CPF"
    def __init__(self, cpf):
        # if (not self.validate_cpf(cpf)):
        #     raise CpfInvalido
        # else:
        self.cpf = cpf
     

    def validate_cpf(self,cpf):
        ''' Expects a numeric-only CPF string. '''
        if len(cpf) < 11:
            return False    
        
        if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
            return False
        
        calc = lambda t: int(t[1]) * (t[0] + 2)
        d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
        d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
        return str(d1) == cpf[-2] and str(d2) == cpf[-1]

class AuditoriaCorrentistas:
    """ Concentra todas as operações de correntistas, identificadas pelo cpf
        Deve permitir a entrada de registros de depósito e saque, identificada por CPF
        Deve possuir a capacidade de retornar a lista com todos os registros para um CPF específico """
        
    def __init__(self)
        self.lista =[]

    def adicionar_registros(self, Cpf, historico):
        self.lista.append()


    def listar(self):


class Correntista:
    """ Classe correntista """
    def __init__(self, codigo, nome, Cpf, saldoinicial):
        self.codigo = codigo
        self.nome = nome
        self.saldo = 0
        self.Cpf = Cpf
        self.historico = []
        self.deposita(saldoinicial)
    
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


class Principal:
    def __init__(self):
        self.__listac = []
        self.__correntistaAtual = None

    def displayCorrentistas(self):
        for c in self.__listac:
            print('Codigo: {}, Nome: {}, CPF: {}, Saldo: {}'.format(c.codigo, c.nome, c.Cpf.cpf, c.saldo))
        print('=' * 10)
        print('Escolha um correntista:')
        opcao = input()
        return int(opcao)

    def displayMenu(self):   
        clear()
        print('Operações')
        print('='* 10)
        print('1 - Cadastrar correntista')
        print('2 - Selecionar correntista')
        print('3 - Sair')
        opcao = int(input())
        return opcao

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
           

    def displaySubMenu(self):   
        clear()
        print('Operações para o correntista => "{}"'.format(self.__correntistaAtual.nome))
        print('Codigo: {}, Nome: {}, Saldo: {}'.format(self.__correntistaAtual.codigo, self.__correntistaAtual.nome, self.__correntistaAtual.saldo))
        print('='* 10)
        print('1 - Fazer Depósito')
        print('2 - Fazer Saque')
        print('3 - Ver Histórico')
        print('4 - Menu principal')

        opcao = int(input())
        return opcao

    def findCorrentista(self, codigo):
        correntista = None
        for c in self.__listac:
            if c.codigo == codigo:
                correntista = c
                break
        return correntista

    def displayHistorico(self):
        for hist in self.__correntistaAtual:
            print("Operacao: {}, Valor: {}".format(hist.operacao, hist.valor))


    def executa(self):  
        while True:
            try:
                opcao = int(self.displayMenu())
                if opcao == 1:
                    self.cadastrarCorrentista()
                elif opcao == 2:
                    if len(self.__listac) == 0:
                        raise ListaVazia 
                    codigo = self.displayCorrentistas()
                    self.__correntistaAtual = self.findCorrentista(codigo)
                    if self.__correntistaAtual == None:
                        print('Correntista não encontrado.')
                        input()
                    else:
                        opcao = self.displaySubMenu()
                        if opcao == 1:
                            print('Digite o valor do depósito:')
                            deposito = int(input())
                            self.__correntistaAtual.deposita(deposito)
                        elif opcao == 2:   
                            print('Digite o valor do saque:')
                            saque = int(input())
                            self.__correntistaAtual.saque(saque)
                        elif opcao == 3:   
                            self.displayHistorico()
                            input()
                elif opcao >= 3:
                    break
            except SaldoNegativo:
                print('O correntista {} ficará com saldo negativo. Operação não executada.'.format(self.__correntistaAtual.nome) )    
                input()
            except OpcaoInvalida:
                print('Opção inválida.')    
                input()
            except ListaVazia:
                print('Não há correntistas cadastrados.')    
                input()
            except ValueError:
                print('Opção inválida.')    
                input()
            except Exception as e:
                print("outra exceção:" + e.__class__.__name__ )    
                print("Mensagem:" + str(e))
                input()

if __name__ == '__main__':
    print('execução pelo terminal')
    sistema = Principal()
    sistema.executa()
else:
    print('execução como módulo')    

