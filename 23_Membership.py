#Membership operator
#list tuple dict set
#in
#not in

list1 = [1,2,3,4,5,'w']
list2 = [1,2,3,4,5]
print( 1 in list1)

if "w" in list1:
    print("w is in list")
print(6 not in list2)

x = 24
y = 20
myList = [10,20,30,40,50]
if x not in myList:
    print("x not in given myList")
else:
    print("x is present in given my list")
if y in myList:
    print("y is in myList")
else:
    print("y is not in myList")

list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

def overlap(list1, list2):
    c = 0
    d = 0
    for i in list1:
        c += 1
    for i in list2:
        d += 1
    for i in range(0,c):
        for j in range(0,d):
            if list1[i] == list2[j]:
                return 1
    return 0
    
if(overlap(list1, list2)):
    print("they are overlap")
else:
    print("they are not overlap")

