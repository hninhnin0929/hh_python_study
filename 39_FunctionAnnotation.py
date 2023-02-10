# def myFun( a:<expression>, b:<expression>)-><expression>:
#function annotation
# annotation -> parameters and return of a function
# docstring-> body of function
# PEP 3107

def myFun(a:'annotation of a', b:'annotation of b')->'return of function':
    """ This is body expression for myFun """
    return a*b

print(myFun.__annotations__)
print(myFun.__doc__)


x = 3
y = 5
def testFun(a:'some value from funCall')->'multiply'+str(max(x,y))+'times':
    """ doc...will return multiply by of max """
    return a*max(x,y)

data = testFun(2)
print(data)
print(testFun.__doc__)
print(testFun.__annotations__)