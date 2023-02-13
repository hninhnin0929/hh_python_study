#callable , if can call => true, not =>false

# print(callable(print))
# print(callable('xyx'.upper))

# test = print('hello')
# print(test)

# al = [1,2,3,4]
# result = al.append(5)
# print(al)
# print(result)

#print len, callable
#str.upper, list.append
#def lambda : expression

from decimal import Decimal

print(callable(Decimal))
#some objs are callable, some are not
a = Decimal('10.10')
print(type(a))
print(callable(a))

class myClass:
    def __init__(self, x=0):
        print('from class')
        self.counter = x

    def __call__(self, x=1) :
        print('upddating value........')
        self.counter += x

    def myFun(self, z=20):
        print('This is my fun............')
        self.counter += z

myobj = myClass()
# print(myobj)
# print(callable(myobj))

print(myClass.__call__(myobj,10))
print(myobj.counter)
myobj()
print(myobj.counter)
print(callable(myobj))

inobj = myClass()
print(myClass.__init__(inobj,20))
print(inobj.counter)
inobj()
print(inobj.counter)
print(callable(inobj))


myfunobj = myClass()
print("..............................")
print(myClass.myFun(myfunobj, 30))
print(myfunobj.counter)
myfunobj()
print(myfunobj.counter)
print(callable(myfunobj.myFun))