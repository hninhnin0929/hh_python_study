
#returning function from a function

def square(a):
    return a**2

def cube(b):
    return b**3

def num(number):
    if number == 1:
        return square
    else:
        return cube

def funTofun(fun1,n):#function name, number some
    return fun1(n)

a = funTofun(cube,3)
b = funTofun(square,10)
print('callin cube function ', a)
print('callin square function ', b)

sq = num(1)
print(type(sq))
print(sq(10))

cu =  num(2)
print(cu(10))