#end of positional arguments
#**

def myFun(a,b, *,c):
    print(a,b,c)

myFun(1,2,c=10)

def myFun1(**key): #will return as dictionary
    print(key)

myFun1(a=10,b=20,c=30)

#end of positional argument(keywork only argument) keyword arguments

def myFun2(a,b,*,koa,**kw):
    print(a)
    print(b)
    print(kw)
    print(koa)

myFun2(a=10,b=20,c=30,koa=101)
