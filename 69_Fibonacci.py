#memorization

def fibo(n):
    print('Calculating fibo {0}'.format(n))
    return 1 if n < 3 else fibo(n-1)+fibo(n-2)

print(fibo(6))