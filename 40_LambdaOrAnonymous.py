#Anonymous function
#Lambda expression or anonymous

def myFun(y):
    return y*2


x = lambda y:y*2

print(x(3))


a = lambda y,z=10:y*z

print(a(2,2))
print(a(2))

b = lambda x,*args,y,**kwargs:(x,args,y,kwargs)
print(b(10,'a','b',y=10,i=10,j=20,k=30))