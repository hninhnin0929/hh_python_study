class Parent:
    pass
class Child(Parent):
    pass

print(issubclass(Child, Parent))
objOfChild = Child()
print(isinstance(objOfChild, Child))
print(isinstance(objOfChild, Parent))