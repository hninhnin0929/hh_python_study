from myModule import fibo, listFibo

fibo(10)
#delete Moddulee
del globals()['myModule']
fibo(100)