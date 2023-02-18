from functools import partial

def myFun(x,y,*arg,x1,y1,**kwargs):
    print(x,y,arg,x1,y1,kwargs)

newFun = partial(myFun, 10, 20, x1='test')

newFun( 30, 40, y1='hello', aa=100, bb=200)


def pow(base, exponent):
    return base ** exponent

sq = partial(pow, exponent=2)
print(sq(2))
cu = partial(pow, exponent=3)
print(cu(2))

print("testing for base with 5 and exponent 3 = " , cu(base=5))