# closure is inserting data to function without passing parameters
# must have nested function
# if you delete outeeer fun, closure func can memorize its data
# inner func var must refer to outer func's data
# is used  when reducing global variables
# hiddeen its data
# to be more less funcs

def myFun():
    data = "I am belong to myFun "
    def myFun2():
        print(data)
    return myFun2

obj1 = myFun()
# obj1()
del myFun
# myFun()
obj1()

def myFun1(n):
    def adding(data):
        return data + n
    return adding

add10 = myFun1(10)
add20 = myFun1(20)
print('This will be added 10 = ', add10(20))
print('This will be added 20 = ', add20(20))
print('This will be add10 obj ', add20(add10(5)))
