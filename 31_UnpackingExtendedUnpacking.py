#unpacking
#extended unpacking

a, *b = [1,2,3,4,5,6,7] #*
print(a)
print(b)

a, *b = 'greenhackers'
print(a)
print(b)

a, *b, c = 'greenhackers'
print(a)
print(b)
print(c)

l1 = [1,2,3]
l2 = [4,5,6]
list =[l1, l2]
print(list)
li = [*l1, *l2]
print(li)

# print('------------------------')
# a, *b, (c,*d, e) = [1,2,3,'winhtut']
# print(a)
# print('------------------------')
# print(b)
# print('------------------------')
# print(c)
# print('------------------------')
# print(d)
# print('------------------------')
# print(e)
# print('------------------------')

print('------------------------')
a, *b, (c,*d, e),[z,*x,y] = [1,2,3,'winhtut','greenhackers']
print(a)
print('------------------------')
print(b)
print('------------------------')
print(c)
print('------------------------')
print(d)
print('------------------------')
print(e)
print('------------------------')
print(z)
print('------------------------')
print(x)
print('------------------------')
print(y)
print('------------------------')

index = [1,2,3,'winhtut','greenhackers']
print(index[0])
print(index[1:-1])
print(index[:])