# def bShop(name, quantity, unit, tList=[]):
#     tList.append('{0} {1} {2}'.format(name,quantity,unit))
#     return tList

def bShop(name, quantity, unit, tList=None):
    if not tList:
        tList = []
    tList.append('{0} {1} {2}'.format(name,quantity,unit))
    return tList

store1 = bShop('java',1,'book')
bShop('python',2,'book',store1)
store2 = bShop('c++',3,'book')
bShop('js',4,'book')
bShop('assembly',5,'book',store2)
bShop('golang',10,'book',store1)

print(store1)
print(store2)


if store1 is store2:
    print("they are the same")
else:
    print("they are not the same")