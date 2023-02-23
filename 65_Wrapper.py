#wraps
from functools import wraps

def log(fn):
    @wraps(fn)
    def with_log(*args, **kwargs):
        print(fn.__name__ + " was called")
        return fn(*args, **kwargs)
    return with_log

@log
def myFun(x):
    """Some operation just like arith"""
    return x+x+x
@log
def myFun2(x):
    """from myfun 2"""
    return x+x+x

myFun(5)
print(myFun.__name__)
print(myFun.__doc__)

myFun2(10)