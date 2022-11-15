a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(id(a), id(b))

value = a is b
print(value)

if a==b :
    print('they are same value')
else:
    print('they are not in same location')

#namespace 
#global namespace
#local namespace
#builtin namespace
from math import log2, log10, log1p
a = 20
def outerfun():
    print(a)
    a = 20 #global namespace
    b = 30 #local namespace
    def innerFun():
        print(a)
        a =30