#import Fibonacci as fb
#from Fibonacci import * ## nao usar esta opção import * -- nomes que começam com _ nao sao importados (métodos private)
from Fibonacci import Fibonacci as fb

if __name__ == '__main__':  # main será sempre o módulo que é invocado, nunca os importados.
    import sys
    #x = int(sys.argv[1])   
    x = 100
    lista = []
    for n in range(0,x):
    #fib = fb.Fibonacci(n)
        fib = fb(n)
        if fib <= 100:
            lista = lista + [fib]
        else:
           break
    print(lista)
##print(fb.__name__)

#Pacotes - sao uma maneira de estruturar o "espaço de nomes" dos módulos python, usando "nomes de modulo com pontos"
#por exempolo, "A.B.C" define um módulo C
## __init__.py = para saber que aquela pasta é um pacote

## _init__.py = é necessario que o python reconheca a pasta como sendo um package

# import sound.effects.echo
# from sound.effects import echo
# from sound.effects.echo import echofilter
