#Variable are Memory Reference
#How they are allocated in program memory
#What is memory reference
#What is memory address in C

#id()
#Differenct between Python And C
#hex()

#Stack Memory and Heap Memory
#Stack Memory=> Function and Methods
#Heap Memory=> Objects

#data=10            data=0x1008(reference)-->>10(object)

a = 10
b = 10
print(id(a)) #output memory address #decimal value
print(hex(id(a)))   #hexa decimal value
print(hex(id(b)))  #as same value, same memory allocation
if id(a) ==  id(b):
    print("They are same memory address ,", id(a))
else:
    print("They are not same memory address")
