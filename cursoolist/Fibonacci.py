def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num -1) + Fibonacci(num -2)
        
        
if __name__ == '__main__':
    print('sou o main do fibonacci')
else:
    print('estou sendo importado: ' + __name__)    