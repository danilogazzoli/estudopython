def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num -1) + Fibonacci(num -2)

lista = []
for n in range(0,100):
    fib = Fibonacci(n)
    if fib <= 100:
        lista = lista + [fib]
    else:
        break

print(lista)
