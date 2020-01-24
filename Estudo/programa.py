#coding: utf-8

print("meu 'primeiro' programa \nesta é a segunda linha de código.")
print("este é um exemplo de \"escape\".")
print("hoje é o dia 10\\10\\2019.")
print('adiciona\b backspace')
print('adiciona um form feed \f')
print('adiciona um \rcarriage return')
print('adiciona um código unicode \u265A')

mensagem = 'esta é uma mensagem em python'
nro = 5
pi = 3.14

print('*'*10+'Funções de string'+'*'*10)
print(mensagem.lower())
print(mensagem.upper())
print('Strings e Listas começam pelo índice 0')

print('A primeira letra da mensagem é {}'.format(mensagem[0]))

print(mensagem.split(' '))
print(type(mensagem.split(' '))) #é uma list

print(nro)
print(pi)

print(type(pi))
print(type(mensagem))
print(type(nro))


print(nro+pi)
print(nro-pi)
print(nro*pi)
print('Divisão com ponto flutuante: {:.2f}'.format(nro/pi))
print('Divisão inteira:', nro//pi)
print(nro**pi) #exponenciação
print(nro % 2) #módulo da divisão


texto = 'texto'

print(mensagem + texto)
print(texto * nro)


print('Para comentar várias linhas de código: selecione as linhas e Ctrl + /')

# numero = int(input('Digite um número: '
#                'Da pra fazer assim?'))

# #print('as instrucoes dentro do if ficam no recuo de 4 espaços')
# if (numero % 2 == 0):
#     print('Número', numero, 'é par')
# else:
#     print('Número', numero,'é impar')

# if (numero % 2 == 0) or (numero % 3 == 0) or (numero % 5 == 0) or (numero % 7 == 0):
#     print('Número não é primo')
# else:
#     print('Número é primo')   

#print('O número digitado foi {}\nO valor do pi é {:.2f}'.format(numero,pi))

print('a função bool retorna false para 0, string vazia e None')
print(bool(0))
print(bool(''))
print((None)) 

x = [1,2,3]
y = [1,2,3]
z = x
print(bool(x == y)) ##verifica conteúdo
print(bool(x is y)) #verifica se é o mesmo objeto
print(bool(z is x)) #verifica se é o mesmo objeto

def IsPrimoWhile(num):
    i = 1
    div = 0
    while (i <= num):
        if num % i == 0:
            div=div+1
        i=i+1
    return bool(div == 2)

def IsPrimoFor(num):
    div = 0
    for i in range(1,num+1):
        if num % i == 0:
            div=div+1
            if div > 2:
                break
    return bool(div == 2)


# if IsPrimoFor(numero):
#     print('número é primo')
# else:
#     print('não é primo')

primos = []
for x in range(1,100):
    if IsPrimoFor(x):
        primos = primos + [x]
        #print(x)

print('Existem {} números primos de 1 a 100'.format(len(primos)))
print(primos)
print('O maior primo é {} e o menor é {}'.format(max(primos),min(primos)))
print('o primeiro valor da lista é {}'.format(primos[0]))

# exemplos com listas

listastr = ['a', 'b', 'c']
listaint = [1,2,3]

listaheterog=[]
for i in range(0, len(listastr)):
    listaheterog.append(listastr[i])

for i in range(0, len(listaint)):
    listaheterog.append(listaint[i])

print(listaheterog)

listaheterog.extend(['mais um elemento', 'outro elemento'])
print(listaheterog)

listastr = list('Danilo')

print(listastr)
print(listastr[0:3])

print(listastr[2:])

nome = 'Food network'
print(nome[0:4])

sequencia = range(1,3)

print(sequencia)

for y in sequencia:
    print(y)

#sets

abcx = set('abacaxi') 
abct = set('abacate')

print(abcx)
print(abct)

print(abcx - abct) #o que tem em abcx e nao em abct
print(abcx | abct) #uniao
print(abcx & abct) #intersecção


#dicionarios

pessoa = {'nome':'Danilo', 'idade':40, 'RG': '123456'}
print(pessoa)
print(pessoa['nome'])

print(pessoa.keys())

print(pessoa.values())

print('Este é um exemplo de print com %s' %('%s')) 
print('Este é um exemplo de print com %s' %(100)) 

"""
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
"""

people = {'02639086901': {'Movimentacao': []},
          '01400517915': {'Movimentacao': []}}

mov = []
mov.append('a')
mov.append('b')
people['02639086901'] = {'Movimentacao': mov}

mov.append('c')
mov.append('e')
mov.append('d')

people['00502117944'] = {'Movimentacao': mov}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    
    for key in p_info:
        print(key + ':', p_info[key])
print('*'*30)        
print(people.values())        
print(people.keys())        