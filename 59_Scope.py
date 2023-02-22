#Scope Of VARIABLE
#Scope global, local
#NonLocal variable

g = 10
def myFun(n):
    global g    # it makes changes to global var, if not, no change in global
    g = 20
    v = g ** 2
    return v

print(myFun(2))
print("golbal var g: ", g)

def outerFun():
    d = 'green'
    def innerFun():
        nonlocal d #it makes changes to outer variable, nonlocal
        d = 'python'
        print("InnerFun = ", d)
    innerFun()
    print("OuterFun = ",d)

outerFun()

def outerFun2():
    d = 'green'
    def innerFun1():
        def innerFun2():
            print("The most inner2 ", d)
        innerFun2()
        nonlocal d
        d = "python"
        print("Inner Fun1 ",d)
    innerFun1()
    print('Outer ',d)

outerFun2()