
class AuditoriaCorrentistas:
    """ Concentra todas as operações de correntistas, identificadas pelo cpf
        Deve permitir a entrada de registros de depósito e saque, identificada por CPF
        Deve possuir a capacidade de retornar a lista com todos os registros para um CPF específico """
        
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
          cls.__instance = AuditoriaCorrentistas()
        return cls.__instance

    def __init__(self):
        self.lista = {}

    def adicionar_registros(self, Cpf, historico):
        self.lista[Cpf.strcpf] = {'Movimentacao': historico}


    def listar_todos(self):
        count = len(self.lista)
        print('A auditoria possui {} registro(s).'.format(count))
        for p_id, p_info in self.lista.items():
            print("\nCPF:", p_id)
            
            for key in p_info:
                if type(p_info[key]) is list:
                    for item in list(p_info[key]):
                         print("Operação: {}, Valor: {}".format(item.operacao, item.valor))                    
    
    def listar_por_cpf(self, Cpf):            
        if Cpf.strcpf in self.lista.keys():
            print("\nCPF:", Cpf.strcpf)
            for item in self.lista[Cpf.strcpf]['Movimentacao']:
                print("Operação: {}, Valor: {}".format(item.operacao, item.valor)) 
        else:
            print('CPF não encontrado.')        

