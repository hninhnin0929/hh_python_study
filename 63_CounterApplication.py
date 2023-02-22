def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("function {0} was called {1}".format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner

def add(a, b=0):
    """adding two value using decorator"""
    print(a+b)

def sub(a, b=0):
    """sub two valuess using decorator"""
    print(a-b)

resultAdd = counter(add)
resultSub = counter(sub)
resultAdd(10,20)
resultAdd(30,40)
resultAdd(40,50)
resultSub(100, 50)
resultSub(50, 25)