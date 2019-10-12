# _*_ coding: utf-8 _*_

print "------Exercicio 1 ----------------"
var="sou uma string"
print var
x=len(var)/2
print x
var1=var[0:x]
print var1.upper()
var2=var[x:]
print var2.lower()
print "------Exercicio 2 ------------------"

verb=raw_input("Type an English verb: ")
print "The gerund form is " + (verb + "ing").upper()


print "------Exercicio 3 ------------------"
frase=raw_input("Entre com uma frase: ")
x=frase.split(" ")
print "As palavras separadas sao:  ", frase.split(" ")
print "O numero de palavras lidas eh: " + str(len(frase.split(" ")))



print "---- Converta uma temperatura (Celsius ou Farenheit) para a outra medida. -------"
temp=raw_input('Entre com uma temperatura :')
temp=temp.upper()
tempn=int(temp[:-1]) 
if temp.endswith('C'):
  # f=(9*C + (32 * 5)) / 5
    f=(9*tempn + (32*5)) / 5   
    print "A temperatura em Farenheit eh: " + str(f) + "F"
elif temp.endswith('F'): 
  # c=(5*(f-32))/9
    c=(5*(tempn-32))/9
    print "A temperatura em Celsius eh: " + str(c) + "C"
else:
    print "Entrada incorreta"

#---------------------------------------------
print "--- Dado um angulo, informe a qual quadrante o mesmo pertence ---"    
angulo=int(raw_input("Informe um angulo: "))

if (angulo <= 90):
  print "Pertence ao primeiro quadrante"
elif (angulo <= 180):
  print "Pertence ao segundo quadrante"
elif (angulo <= 270):
  print "Pertence ao terceiro quadrante"
else:
  print "Pertence ao quarto quadrante"


#---------------------------------------------
print "Dados tres valores, informe se os mesmos formam um triangulo. Lembrando que: um lado é sempre menor que a soma dos outros dois" 
lado1=int(raw_input("Informe o lado 1: "))
lado2=int(raw_input("Informe o lado 2: "))
lado3=int(raw_input("Informe o lado 3: "))

blado1=(lado1 > abs(lado2 - lado3)) and (lado1 < (lado2 + lado3))
blado2=(lado2 > abs(lado1 - lado3)) and (lado2 < (lado1 + lado3))
blado3=(lado3 > abs(lado1 - lado2)) and (lado3 < (lado1 + lado2))

if blado1 and blado2 and blado3:
  print "É um triangulo"
else:
  print "nao é um triângulo "


#---------------------------------------------
print "Escreva um script que percorra a matriz e mostre seus elementos"

lista1=["nome1","nome2","nome3"]
lista2=[1,2,3]
lista3=[4,5,6,7,8]
m=[lista1,lista2,lista3]

for linha in m:
  for coluna in linha:
    print coluna
  








