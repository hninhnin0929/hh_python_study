#Special Operator
#Identity Operator - is or is no (memory location)
#Membership Operator

a = 10
b = 10
print(id(a))
print(id(b))
c = a is b #check the same memory location
print(c)

if a is b:
    print("They are same location")
else:
    print("They are not same location")

a = 20
if a is not b:
    print("They are not same location")
else:
    print("They are same location")

x = 10
isint = type(x) is int
print("x is integer")

string1 = "hello"
string2 = "hello"

print(id(string1), id(string2))
string3 = string1 is string2
print("The ouput is ", string3)

if string1 == string2:
    print("string 1 and 2 are same")
else:
    print("They are not same")