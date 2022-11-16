#list
#tuple
#set
#dictionary

list = [1,2,3,4,5] #order  order= can get elements by index
tu = (1,2,3,4,5) #order
se = {1,2,3,4,5} #unorder
dic = {'a':10, 'b':20, 'c':30} #unorder

print(list[1])
print(tu[3])
# print(se[1])  it goes error

#unpacking
a,b,c = (10,100,20)
print(a,b,c)

(a,b,c) = [100,200,300]
print(a,b,c)

(a,b,c) = 'XYZ'
print(a,b,c)

dset = {1,2,3,4,5,6}
print(dset)

dset1 = {'a','b','c','d','e'}
print(dset1)
for e in dset1:
    print(dset)


