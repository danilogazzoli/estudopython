def InsertionSort(vetor):
    for i in range(0, len(vetor)):
        chave = vetor[i]
        k = i - 1
        while (k >= 0) and (vetor[k] > chave):
            vetor[k+1]=vetor[k]
            k = k -1
        vetor[k+1] = chave
    return vetor

lista = [9,8,3,4,6,7,5,13,12]

print(InsertionSort(lista))