# _*_ coding: utf-8 _*_

class Pessoa:
  nome_cientifico= "Homo Sapiens"
  def __init__(self, nome, idade):
      self.nome=nome
      self.__idade=idade
  def fazerAniversario(self):
      self.__idade = self.__idade + 1
  def verIdade(self):
      print self.__idade



pessoa1 = Pessoa("Danylow", 25)  
pessoa2 = Pessoa("Pedro", 30)
print pessoa1.nome
print pessoa2.nome

print pessoa1.nome_cientifico
print Pessoa.nome_cientifico

for x in range(20):
    pessoa1.fazerAniversario()

pessoa1.verIdade()    