## Escopo de visibilidade de variável 
def scope_test():
    def do_local():
        spam = "local spam"
 
    def do_nonlocal():
        nonlocal spam ## pertence ao escopo da função da qual está sendo invocada
        spam = "nonlocal spam"
 
    def do_global():
        global spam ## escopo de visibildade pra todo o módulo (module global)
        spam = "global spam"
 
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
 
scope_test()
print("In global scope:", spam)

##################################################

class MyClass:
    """Um exemplo de classe""" #docstring
    i = 1223 ## atributo estático (static - variável da classe, nao da instancia)

    def f(self): ## self nao é um parametro implicito como o self do Delphi, no python tem que explicitar
        return 'hello world'
    
    #construtor da classe
    def __init__(self):
        #Aqui sao os atributos de instancia
        self.atributo = 0

m = MyClass()        
print(m.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.8, -4.5)
print(x.r) 
print(x.i)       