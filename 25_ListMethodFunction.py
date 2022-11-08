subList = ['myanmar', 'math', 'physics','cp']

subList[-1] = 'algorithm'

rm = 'physics'

print(subList)

subList.remove(rm) #with contain value
print('After using remove method\n')
print(subList)

subList.pop(1) #with index
print('After using pop method\n')
print(subList)

del subList[0] #with index
print('After using delete method\n')
print(subList)

subList.append(90)
print(subList)

subList.append('english')
print(subList)

print('length of list' , len(subList))
