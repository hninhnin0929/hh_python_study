def myFun(x,y):
    return x+y

# print(dir(myFun))#return the func's attributes

myFun.__subject__ = 'bio'# add custom attributes
myFun.__mark__ = 90
print(dir(myFun))
print(myFun.__subject__)
print(myFun.__mark__)