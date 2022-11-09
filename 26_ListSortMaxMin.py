numList = [1,2,3,55,100]
print(max(numList))
print(min(numList))
print(numList)
numList.reverse()
print(numList)
myindex = numList.index(55)
print('index of 55 is ', myindex)
sumAllValue = sum(numList)
print('sum of values ', sumAllValue)
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)

charList = ['zoo', 'apple', 'orangee','bell', 'banana']
charList.sort()
print(charList)

charList.sort(key=len)
print(charList)