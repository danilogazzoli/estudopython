import random

arquivo = open('palavras.txt', 'w')
arquivo.write('banana'+'\n')
arquivo.write('melancia')
arquivo.close

arquivo = open('palavras.txt', 'a')
arquivo.write('\nabacaxi')
arquivo.write('\nabacate')
arquivo.write('\nkiwi')
arquivo.write('\npera')
arquivo.write('\n')
arquivo.close

dicion = {'nome':'Danilo', 'sobrenome':'Gazzoli','idade': 42}
rand = random.randrange(0,4)
arquivo = open('palavras.txt', 'a')
arquivo.write(str(dicion) * rand)
arquivo.close

arquivo = open('palavras.txt', 'r')
#lê o arquivo todo
print(arquivo.read())
arquivo.close

arquivo = open('palavras.txt', 'r')
#ler linha a linha 
palavras = []
for linha in arquivo:
    linha = linha.strip() #para tirar espaços em branco no inicio e fim da string
    palavras.append(linha)

print(palavras)
arquivo.close

teste = 'testedepalavra'
count = random.randrange(0, 100)
letras = ['x' for letra in teste]

print(letras)