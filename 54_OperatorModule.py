import operator
from functools import reduce

# print(operator.add(3,5))
# print(operator.mul(3,5))
# print(operator.truediv(3,2))
# print(operator.floordiv(3,2))

list = [1,2,3,4,5,6]
output1 = reduce(lambda x,y: x*y, list)
print("output form the reduce and lamdda :" , output1)

output2 =  reduce(operator.mul, list)
print("output from the reduce and operator : ", output2)

output1 = operator.lt(10, 20)
output2 = operator.gt(10, 20)
output3 = operator.is_('hnin','snow')
output4 = operator.is_not('hnin','snow')
output5 = operator.truth(list)  #there is value in list

print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(dir(operator))