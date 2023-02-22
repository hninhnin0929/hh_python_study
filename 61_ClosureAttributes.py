def myFun1(n):
    def adding(data):
        return data + n
    return adding

add10 = myFun1(10)
add20 = myFun1(20)
print(add10.__closure__)

def test():
    print('heello')
print(test.__closure__)

print(add10.__closure__[0].cell_contents)
print(add20.__closure__[0].cell_contents)