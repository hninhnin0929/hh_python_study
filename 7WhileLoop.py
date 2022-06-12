from cgi import print_arguments


a = 20
b = 20

while a<b:
  print('{} Hello i am hnin'.format(a))
  a += 1

print("Nothing do!")

#break
#continue
#different between break and continue

for va in "winhtut":
  if va == 'i':
    continue
  print(va)
print('----------------ending')

ls = [10,12,13,14,15] #list
data = 10
found = False #flag
index = 0

while index < len(ls):
  if ls[index] == data:
    found = True
    break
  index += 1
  
if not found:
  ls.append(data)
print(ls)