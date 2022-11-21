
def myFun(a,b,c,*args): # a,b,c = positional args, *args = arbitary args or end of postional arguments
    print(a)
    print(b)
    print(c)
    print(args)
    for d in args:
        print(d)

myFun(1,2,3,4,5,6)