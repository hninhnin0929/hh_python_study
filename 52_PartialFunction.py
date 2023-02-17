# def myFun(x,y,z):
#     print(x,y,z)

# def pFunc(yy,zz):
#     return myFun(10,yy,zz)

# pFunc(100,200)

from functools import partial   #reduce arguments

def myFun(x,y,z):
    print(x,y,z)
    x = x+11
    y = y+11
    z= z+11
    print(x,y,z)


newFun = partial(myFun, 10)     #10=pre set value

newFun(100,200)
