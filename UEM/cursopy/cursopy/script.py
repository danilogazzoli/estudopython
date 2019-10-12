------ manipulacao de strings ---------
var1="arquivo.txt"
print var1[:-4]
print var1.upper()
print var1.lower()
print var1.len()
print var1.capitalize()
print var1.title()
print var1.startswith("")
print var1.endswith("")
print var1.find(".")
var1.replace("arquivo","por outra coisa")
var2="segunda, terca, quarta, quinta, sexta"
var2.split(",") 
==>> ['segunda','terca','quarta']

------ listas - vetores ------------
a = ['Gato', 9, True]

--adicionar um elemento
a.append(obj)
-- adicionar ao final da lista
a.extend(obj)
a.extend(['carro',7.4])
a.append(1)
a;remove(1)
--remover um elemento
a.remove(obj)

----- matriz -----------

['a','b','c']
[1,2]
[1,2,3]

------- if ------------

if :
else:


if expressao:
  bçpcp
elif expressao2:
  vcvc
elif expressao3:
  cvvc
else:
  expressao4

----- estruturas de repeticao ----

for i in range(0,10):
  print i

-------
float()
int()
str()
l.append(obj)
l.extend(obj)

-- arquivos --

file = open("nome", "modo")
modos =
  w = escrita
  r = leitura apenas
  a = append
  r+=tanto para leitura quanto para escrita

file.write("string")

file.read()  = retorno o conteudo em uma string

file.read(tamanho) - idem ao read, porém do inicio até o tamanho passado como parametro

arq = open('arq.txt','r')
print arq.read()

file.readline() = realiza a leitura de uma linha do arquivo, começando da primeira e retorna o seu conteúdo em uma string

file.readlines() = lê cada linha do arquivos e as retorna separadamente em uma lista de strings

for linha in arq:
  bloco

file.close()  

file.

-- funcoes --
def nome_da_funcao(parametros):
  "descricao da funcao"
  bloco 

  return[expressao]

def par_impar(x):
  'Esta função retorna se o número é par ou impar'
  if x%2 == 0:
    print 'é par'
  else:
    print 'é impar'  
  return
   

-- OO --

class Pessoa:
  nome_cientifico: "Homo Sapiens"
  




