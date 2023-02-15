def facto(n):
    return 1 if n < 2 else n*facto(n-1) #recursive

# results = map(facto, range(6))
results = list(map(facto, range(6)))  #use list to print next time

print(results)

# for i in results:
#     print(i)
# for x in results:
#     print(x)

list1 = [1,2,3,4,5,6,7,8]
list2 = [10,20,30,40,50]

results1 = list(map(lambda x,y: x+y,list1,list2))
print(results1)
for x in results1:
    print(x)