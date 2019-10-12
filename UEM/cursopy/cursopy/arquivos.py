# _*_ coding: utf-8 _*_
#Ler um arquivo txt, mostrar e contar as suas linhas
print "Dia 2 - Exercício 1"

i = 0
try:
    try:
        arq = open('texto.txt', 'r')
        for linha in arq:
            print linha
            i+=i

        print "O número de linhas é: " + str(i)
    finally:
        arq.close()  
except:
    print "Deu um erro ao tentar abrir o arquivo."


#Dado o arquivo texto passado, onde o mesmo descreve descreve diferentes arquivos,
#faça um script que abra este arquivo e para todas as linhas existentes, informe o nome do arquivo lido 
#e se o mesmo se trata de uma música, imagem, filme ou se é um tipo desconhecido
print "----------------------------------------"
print "Dia 2 - Exercício 2"

try:
    try:
        arq = open('listaarquivos.txt', 'r')
        for linha in arq:
            print linha
            if linha[-4:].lower() == 'mp3\n':
                print "O arquivo {0} é uma música".format(linha)
            elif linha[-4:].lower() == 'avi\n':
                print "O arquivo {0} é um filme".format(linha)
            elif linha[-4:].lower() == 'png\n':
                print "O arquivo {0} é uma foto".format(linha)          
            else:
                print "O arquivo {0} é desconhecido".format(linha)      
    finally:
        arq.close()  
except:
    print "Deu um erro ao tentar abrir o arquivo."



#Faça um programa para ler as últimas "n" linhas de um arquivo
print "----------------------------------------"
print "Dia 2 - Exercício 3"

try:
    arq = open('listaarquivos.txt', 'r')
    numlinha = int(raw_input("Quantas linhas deseja ler? "))
    strings = arq.readlines()

    if numlinha > len(strings):
        print "impossível realizar esta operacao."
    else:
        for i in range((len(strings)-numlinha) , len(strings)):
            print strings[i][:-1]
    arq.close()
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)    


#escreva uma função que leia "n" números, os salve em uma lista e depois some os números

def SomarNumeros(valores = []):
    quant = int(raw_input("Quantos números deseja ler? "))
    for i in xrange(quant):
       valor = int(raw_input("Entre com um número {0}: ".format(i+1)))
       valores.append(valor)
    soma=0   
    for val in valores:
        soma+=int(val)
    return soma

var=[]
print 'A soma dos números é: {0}'.format(SomarNumeros(var))


import sys

def main():


if __name__ == '__main__':
    main()


