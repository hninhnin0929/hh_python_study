import functools


numList = [1,2,3,4,5,6]

print("The sum of all elements from list = ", end="")
print(functools.reduce(lambda a,b: a+b, numList))

print(functools.reduce(lambda a,b: a if a < b else b, numList)) #find min
print(functools.reduce(lambda a,b: a if a > b else b, numList)) #find max