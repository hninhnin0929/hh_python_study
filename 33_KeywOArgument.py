#positional arguments
#arbitary arguments
#keywork only arguments
#end of positional arguments
#**

def myFun(a,b,c):
    print(a)
    print(b)
    print(c)

myList = [1,2,3]
myFun(*myList)


def myFun1(a,b,*c):
    print(a)
    print(b)
    print(c)

myList = [1,2,3,4,5,6,7]
myFun1(*myList)

def myFun2(a,b,*c, d):
    print(a)
    print(b)
    print(c)
    print(d)

myList = [1,2,3,4,5,6,7]
myFun2(*myList, d=8)

def myFun3(*c,d):
    print(c);
    print(d)
myFun3(d='hello')