def AdicionarLista(lista, nome, sobrenome, idade):
    #rec = dict({('nome', nome), ('sobrenome', sobrenome), ('idade',idade)})
    rec = {'nome': nome, 'sobrenome': sobrenome, 'idade':idade}
    lista.append(rec)
    return lista

def Media(lista):
    soma = 0
    count = 0
    for x in lista:
        soma = soma + x
        count = count + 1
    return soma / count 

#main
lista = []

while True:
    nome = input('Nome: ') 
    sobrenome = input('Sobrenome: ')
    idade = int(input('Idade: '))   
    AdicionarLista(lista,nome, sobrenome, idade)
    resp = input('Deseja continuar informando?').lower()
    if not((resp == 's') or (resp == 'sim')):
        break
      

print(lista)

listaNotas = []
for i in range(1, 5):
    nota = int(input('Digite a nota {}: '.format(i)))
    listaNotas = listaNotas + [nota]

print('A média das notas é {}'.format(Media(listaNotas)))

