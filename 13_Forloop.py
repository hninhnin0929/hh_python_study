
#Lesson 13 For Loop
from __future__ import barry_as_FLUFL


l=[10,20,30,40,50]
for i in l:
  print(i)
print('-------------------------')

s='snow'
for i in s:
  print(i)
print('-------------------------')

s = ('a','b','c',3,4,5)
for i in s:
  print(i)
print('-------------------------')


lt=[(1,2),(3,4),(5,6),(7,8)] #packing
for i,j in lt:
  print(i,j)
print('-------------------------')

for i in range(5): #0-4
  if i==3:
    continue
  print(i)
print('-------------------------')

for i in range(1,5): #0-4
  z = i%7
  if z == 0:
    print('multiple of 7 found')
    break
  else:
    print('no multiple of 7 in the range')
print('-------------------------')

for i in range(5): #0-4
  print('###################')
  try:
    z = 10/(i-3)
    print('z = ', z)
  except ZeroDivisionError:
    print('Divided by Zero')
  finally:
    print('always run')
  print(i)
print('-------------------------')

