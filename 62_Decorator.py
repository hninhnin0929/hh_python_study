# add actions to original func or obj without modifying to original func or obj
# do not have the right of modifying
# must have inner func

def myFun(x,y):
    print(x/y)

def working(fn):
    def inner(x,y):
        if x < y:
            x,y = y,x
        return fn(x,y)
    return inner

result = working(myFun)
result(5,10)
