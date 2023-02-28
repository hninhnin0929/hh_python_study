#class
#object = reference of a class( refs a class)
#attribute = variable in class
#behavior = methods in class

class MyClass: #python enhancement proposals 8,PEP 8
    pass

obj1 = MyClass()
obj2 = MyClass()
print(obj1)
print(obj2)

if id(obj1) == id(obj2):
    print("They are same")
else:
    print("Not same")