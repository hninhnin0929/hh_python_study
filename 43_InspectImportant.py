
import inspect
from inspect import isfunction, ismethod
import math

def myFun(x,y,z=10,*,kw1,kw2=2):
    return x+y

print(myFun.__name__)# namee
print(myFun.__defaults__) #positional args
print(myFun.__kwdefaults__)#keywords only arguments
print(myFun.__code__.co_varnames)
print(myFun.__code__.co_argcount)#count positional args

print(inspect.getsource(myFun))
print(inspect.getcomments(myFun))
print('checking is function ', isfunction(myFun))
print('checking is method ', ismethod(myFun)) #it exists under control of the class

# class hello:
#     myFun(): #method

# def myFun(): #function

print(inspect.getmodule(print))
print(inspect.getmodule(ismethod))
print(inspect.getmodule(math.sin))