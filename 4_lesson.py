#control structure
#if
#if else
#elif
#largest number sample program

a=10
b=20
c=30
if a<b : 
  print('a < b')
elif a==b:
  print('a==b')
else: 
  print('a > b')

#largest number
a=150
b=85
c=91
d=100
e=10

if (a>b) and (a>c) and (a>d):
  largestNumber =a
elif (b > a) and (b>c) and (b>d):
  largestNumber=b
elif (c > a) and (c>c) and (c>d):
  largestNumber=c
else:
  largestNumber=d
print("largest number is ", largestNumber)


