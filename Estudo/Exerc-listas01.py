#1 - dada a lista abaixo

# imprima a maior elemento

def MaiorElemento(numlist):
    maior = 0
    for x in numlist:
        if x > maior:
            maior = x
    return maior

def MenorElemento(numlist):
    menor = 0
    for x in numlist:
        if x < menor:
            menor = x
    return menor

def RetornaPares(numlist):
    pares = []
    for x in numlist:
        if x % 2 == 0:
            pares += [x]
    return pares

def RetornaOcorrencias(numlist):
    prim = numlist[0]
    count = 0
    for x in numlist:
        if x == prim:
            count += 1
    return count

def Media(numlist):
    count = 0
    soma = 0
    for x in numlist:
        count = count + 1
        soma += x
    return soma // count

def SomaNegativos(numlist):
    soma = 0
    for x in numlist:
        if x < 0:
            soma += x
    return soma


# main()
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17,2,12,8,3,3,-52]
print('Maior elemento da lista é {}'.format(MaiorElemento(lista)))

print('Menor elemento da lista é {}'.format(MenorElemento(lista)))

print(RetornaPares(lista))

print(RetornaOcorrencias(lista))

print(Media(lista))

print(SomaNegativos(lista))