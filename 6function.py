#Function
#Standard Library Function -ori
#Programmar Defined Function -us

from math import sqrt
import math

# ls = [1,2,3,4,5]
# print("The length of ls is " , len(ls))
# print("the square root of ", sqrt(4))

# data = int(input("Please enter number to sqrt "))
# print("The square root of {} is {}".format(data,sqrt(data)))
# print("the value of pi is ", math.pi)
# print("the exp of {} is {}".format(data, math.exp(data)))
# print("the hex value of {} is {}".format(data, hex(data)))

# def myFun():
#   print("i am from myFun")

# print("function calling ", myFun())

def add(a,b): #function header a,b = parameter
  return a+b

def sub(a,b):
  return a-b

def multi(a,b):
  return a*b

def divi(a,b):
  return a/b

fdata = int(input("please enter first number: "))
sdata = int(input("please enter second number: "))
print("adding = ", add(fdata,sdata))
print("subtracting = ", sub(fdata,sdata))
print("multiplying =", multi(fdata,sdata))
print("dividing = ", divi(fdata,sdata))