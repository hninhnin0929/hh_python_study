def myDec_1(fn):
    def inner():
        print(' running decorator 1')
        return fn()
    return inner 
    
def myDec_2(fn):
    def inner():
        print(' running decorator 2')
        return fn()
    return inner

# @myDec_1
@myDec_2    #same to=> result = myDec_1(myDec_2(myFun))
def myFun():
    print('running my fun')

# result = myDec_1(myDec_2(myFun))
# result()

myFun()

