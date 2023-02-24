#least recently used lru_cache
from functools import lru_cache

@lru_cache(maxsize=3)  # it means we will use cache 5 , #maxsize=128, none
def fib(n):
    print('Calculating fib{0}'.format(n))
    return 1 if n < 3 else fib(n-1)+fib(n-2)
print(fib(5))
print('after printing fib 5....')
# print(fib(10)) #delete 1-5, restore 6-10
# print('after printing fib 10....')
print(fib(7))
print(fib(5))