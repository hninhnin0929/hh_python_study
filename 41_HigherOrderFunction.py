def myFun(x,fn):    #higher order function
    return fn(x)

value = myFun(5, lambda y: y**2)
print(value)


def myFun1(fn, *args, **kwargs):
    return fn(*args, **kwargs)

value = myFun1(lambda x,y: x+y, 2,y=20)
print(value)