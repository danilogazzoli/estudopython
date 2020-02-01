from correntista import Correntista
from cpf import Cpf
import os
from excecoes import ListaVazia
from excecoes import SaldoNegativo
from excecoes import OpcaoInvalida
from auditoriaCorrentistas import AuditoriaCorrentistas
from banco import Banco

clear = lambda: os.system('clear')


class Principal:
    def __init__(self):
        self.__banco = Banco()
        self.__correntistaAtual = None

    def display_correntistas(self):
        self.__banco.display_correntistas()
        print('=' * 10)
        print('Escolha um correntista:')
        opcao = input()
        return int(opcao)

    def display_correntistas_por_nome(self):
        print('Digite uma parte do nome:')
        nome = input()
        lista = self.__banco.find_correntista_por_nome(nome)
        if len(lista) > 0:
            print('=' * 10)
            print('Escolha um correntista:')
            opcao = int(input())
            return int(opcao)
        else:
            print('Não foi encontrado nenhum correntista com este nome.')
            input()
            return None

    def cadastra_correntista(self):
        print('Digite o nome:') 
        nome = input()
        print('Saldo inicial:')
        saldoinicial = int(input())
        print('CPF:')
        cpf = input()
        cp = Cpf(cpf)
        cont = self.__banco.get_correntistas_count
        print('cont 2:{}'.format(cont))
        c = Correntista((cont + 1),  nome, cp, saldoinicial)
        print(c.serialize())
        input()

        self.__banco.cadastra_correntista(c)

    def displayMenu(self):
        clear()
        print('Operações')
        print('=' * 10)
        print('1 - Cadastrar correntista')
        print('2 - Selecionar correntista por Código')
        print('3 - Selecionar correntista por Nome')
        print('4 - Exibir a auditoria')
        print('5 - Listar auditoria por CPF')
        print('6 - Listar auditoria serializado')
        print('7 - Sair')
        opcao = int(input())
        return opcao

    def displaySubMenu(self):
        clear()
        print('Operações para o correntista => "{}"'.format(self.__correntistaAtual.nome))
        print('Codigo: {}, Nome: {}, Saldo: {}'.format(self.__correntistaAtual.codigo, self.__correntistaAtual.nome,
                                                       self.__correntistaAtual.saldo))
        print('=' * 10)
        print('1 - Fazer Depósito')
        print('2 - Fazer Saque')
        print('3 - Ver Histórico')
        print('4 - Menu principal')

        opcao = int(input())
        return opcao

    def displayHistorico(self):
        for hist in self.__correntistaAtual:
            print("Operacao: {}, Valor: {}".format(hist.operacao, hist.valor))

    def findCorrentista(self, codigo):
        return self.__banco.find_correntista_por_codigo(codigo)

    def movimentaCorrentista(self):
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

    def executa(self):
        while True:
            try:
                opcao = int(self.displayMenu())
                if opcao == 1:
                    self.cadastra_correntista()
                elif opcao == 2:
                    codigo = self.display_correntistas
                    self.__correntistaAtual = self.findCorrentista(codigo)
                    self.movimentaCorrentista()
                elif opcao == 3:
                    codigo = self.display_correntistas_por_nome()
                    if codigo is not None:
                        self.__correntistaAtual = self.findCorrentista(codigo)
                        self.movimentaCorrentista()

                elif opcao == 4:
                    audit = AuditoriaCorrentistas()
                    audit.get_instance().listar_todos()
                    input()
                elif opcao == 5:
                    print('Digite o CPF:')
                    cpf = str(input())
                    c = Cpf(cpf)

                    audit = AuditoriaCorrentistas()
                    audit.get_instance().listar_por_cpf(c)
                    input()
                elif opcao == 6:
                    audit = AuditoriaCorrentistas()
                    print(audit.get_instance().serialize())
                    input()
                elif opcao >= 7:
                    break
            except SaldoNegativo:
                print('O correntista {} ficará com saldo negativo. Operação não executada.'.format(
                    self.__correntistaAtual.nome))
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
                raise
                # print("outra exceção:" + e.__class__.__name__)
                # print("Mensagem:" + str(e))
                input()


if __name__ == '__main__':
    print('execução pelo terminal')
    sistema = Principal()
    sistema.executa()
else:
    print('execução como módulo')
