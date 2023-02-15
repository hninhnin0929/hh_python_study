# def myFun(x):
#     return x    #terminate

# def myGen(g):
#     yield g     #suspend


def myGen():
    data = 10
    yield data
    yield data+1
    yield data+2
    yield data+3

result = myGen()
print(result)
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
for i in result:
    print(i)

def genTest():
    x = 1
    while x<= 10:
        square = x*x
        yield square
        x+=1
results = myGen()
for i in results:
    print(i)


