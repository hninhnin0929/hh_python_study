
charList = ['zoo', 'apple', 'orangee','bell', 'banana']

for element in charList:
    if(element == 'zoo'):
        print(element)
    else:
        print('zoo not found')

numList = [1,2,3,4,5,6,7,8]
for element in numList:
    element += 3
    print(element)

for element in numList[:3]:
    numList.remove(element)
    print('removing ', element)
print(numList)

numList = []
for element in range(1,10):
    data = element**2
    numList.append(data)
    print('appending =',data)

print(numList)

numTuple = (1,2,3,4,5,6)
print(numTuple)
print(list(numTuple))
