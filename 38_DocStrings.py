#docstring
#document string

def myFun(x,y):
    #'this is testing' #comment is not known by python interpreter
    """ This 'function' returns x*y """ #must be the first line except comment
    return x*y

myFun(1,2)
help(myFun)
print(myFun.__doc__)