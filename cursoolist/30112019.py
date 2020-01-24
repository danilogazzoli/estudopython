#implementar uma função que receba uma lista e retorne uma lista apenas com elementos únicos (remova os duplicados)

def funcaoRemoveDuplicados(lista):
    ListaUnicos = []
    for x in lista:
        if x not in ListaUnicos:
           # ListaUnicos += x
           ListaUnicos.append(x)

    return ListaUnicos

lista = [1,2,2,3,3,3,6,6,6,9,9,9,9]

print(funcaoRemoveDuplicados(lista))


#crie uma função que receba uma string e retorna ao contrário

def ReverseString(s):
    rv = ''
    for ch in s[::-1]:
        rv = rv + ch
    return rv

'''
def ReverseString2(s):
    rv = ''
    index = len(s)
    while index > 0:
        rv += s[index -1]
        index = index - 1
    return rv    
'''

s = 'Danilo'    
print(ReverseString(s))

#Tuplas
# Tupla é um objeto do tipo sequencial, imutável, geralmente utilizado para armazenamento de dados heterogêneos(tipos diferntes)

a = () #tupla vazia
b = 1, #tupla de um titem
c = (1,)
d = tuple()

#Dicionários é um objeto de mapeamento, mutável, que utiliza objetos hashable como chave de mapeamento para objetos arbitrários e heterogêneos
a = dict(one =1, two=2, three=3)
b = {'one':1, 'two': 2, 'three': 3}
c = dict([('two', 2), ('one', 1), ('three', 3)])
d = dict({'three': 3,  'one': 1, 'two': 2})


# listas = []
# tuplas = ()
# dicionarios = {}

#zip faz a "costura" das duas tuplas
c = dict(zip(['one', 'two', 'three'],[1,2,3]))
print(c)
# {'one': 1, 'two': 2, 'three': 3}

#funcoes variádicas
# funções podem ser defindias de modo a aceitar um número arbitrário de argumentos

def func_variadic(param, *args):
    print('param', param)
    for arg in args:
        print(arg)

func_variadic("test", "More", "and", "arguments")

#parametros passados depois do *args, sempre usar os próximos parâmetros com default
def concat(*args, sep='/'):
    return sep.join(args)

s = concat('earth', 'mars', 'venus')
print(s)
s = concat('earth', 'mars', 'venus', sep='.')
print(s)

def func_var_keyword(param, **keywords): #**keywords é um dicionario
    print("param:", param)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    #print(type(**keywords))    

func_var_keyword("test",
                  kwa = 'A',
                  kwb = 'B',
                  kwc = 'C' )       


def func_var_full(param, *args, **keywords): #**keywords é um dicionario
    print("param:", param)
    print("-"*40)
    for arg in args:
        print(arg)    
    print("-"*40)    
    for kw in keywords:
        print(kw, ":", keywords[kw])
    #print(type(**keywords))                   

func_var_full('teste', 'earth', 'mars', 'venus', kwa = 'A',
                  kwb = 'B',
                  kwc = 'C' )    

#desempacotamento de listas de argumentos
# uma lista de argumentos pode ser passado utilizando o operador *
list(range(3,6))
args = [3,6]
print(list(range(*args)))

def add(a=0, b=0):
    return a + b
d = {'a': 2, 'b': 3 }

print(add(**d))

'''
def teste(a, b, c):
    lista = [a,b,c]
    print(lista)
   
teste(1, 2, 3)

'''

# PEP 8 - boas práticas do python

# use identacao com 4 espacos, e nao use tabs
# quebre as linhas de modo que nao excedam 79 caracteres
# Deixe linhas em branco para separar funções e classes, e blocos de código dentro de funções
# quando possível, coloque comentŕios em uma linha própria
# escreva strings de documentação = usando docstring ''' documentacao '''
# use espacos sao redor de operadores e apos virgulas, mas nao diretamente dentro de parentses, colchetes e chaves.
# a = f(1,2) + g(3,4)
# nomeie suas classes e funcoes de forma consistente, a convencao é usar MaiusculoCamelCase para classes e minusculo_com_underscore para funcoes e metodos. 
# Sempre use self como o nome para o primeiro argumento dos métodos (veja Primeiro contato com classes para mais informações sobre classes e métodos)
# Nao use codificacoes exoticas se o seu codigo é feito para ser usado em um contexto internacional. o padrao do python, UTF-8, ou mesmo ASCII puro funciona bem em qualquer caso.
# Da mesma forma, nao use caracteres nao-ASCII em identificadores 

# realpython.com/python-pep8

# entrada numero, a saída será o número de listas pela quantidade de vezes do número da entrada
# exemplo:
# entrada 1 / saída = [1]
# entrada 2 / saida = [1,2],[3,4]
# entrada 3 / saida = [1,2,3],[3,5,6],[7,8,9]

def func_entrada(n):
    num = 0
    listamaior = []
    for j in range(0,n):
        lista = []
        for i in range(0,n):
            num += 1
            lista.append(num)
        listamaior.append(lista)
    return listamaior

print(func_entrada(4))

#modulo sao arquivos "py". contendo declaracoes e definicoes. Todos arquivo de codigo python pode ser considerado um módulo
