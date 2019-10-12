def calculadora(x,y):
    return {'soma': x+y, 'mult': x * y, 'div': x / y, 'sub': x - y}

def calculadoraVariosRetornos(x,y):
    return x+y, x * y, x / y, x - y

def velocidade_media(distancia, tempo):
    return distancia / tempo

## main
print(calculadora(4,5))
print(type(calculadora(4,5)))

print(calculadoraVariosRetornos(10, 30))
print(type(calculadoraVariosRetornos(10, 30)))

print('Velocidade {}'.format(velocidade_media(100, 10)))

