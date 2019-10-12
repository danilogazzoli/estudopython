def calculadora(x,y):
    return {'soma': x+y, 'mult': x * y, 'div': x / y, 'sub': x - y}

def calculadoraVariosRetornos(x,y):
    return x+y, x * y, x / y, x - y

def velocidade_media(distancia, tempo):
    return distancia / tempo

def teste(arg, *args):
    print('O primeiro argumento é: {}'.format(arg))
    for arg2 in args:
        print('os outros são: {}'.format(arg2))

## main
print(calculadora(4,5))
print(type(calculadora(4,5)))

print(calculadoraVariosRetornos(10, 30))
print(type(calculadoraVariosRetornos(10, 30)))

print('Velocidade {}'.format(velocidade_media(100, 10)))

teste('este é um teste', 1, 2, 3, 'vários argumentos')

lista = ["a", 'b', 'c']
teste('param1', *lista)

