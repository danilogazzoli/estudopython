import json

class Cpf:
    "classe para validação de CPF"
    def __init__(self, cpf):
        # if (not self.validate_cpf(cpf)):
        #     raise CpfInvalido
        # else:
        self.__cpf = cpf
     

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

    @property
    def strcpf(self):
        return self.__cpf      

    def serialize(self):
        return {'cpf': self.__cpf}    
    
    @classmethod
    def deserialize(cls, data):
        print(data)
        return Cpf(data['cpf'])


