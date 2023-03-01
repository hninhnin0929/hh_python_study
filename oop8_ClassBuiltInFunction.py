#class built in function
# getattr(obj, name)
# setattr(obj, name, value)
# delattr(obj, name)
# hasattr(obj, name)

class Student:
    def __init__(self, name, id, age) -> None:
        self.name = name
        self.id = id
        self.age = age

sobj = Student("Hnin", 101, 25)
print(getattr(sobj, 'name'))
print(getattr(sobj, 'age'))
setattr(sobj, 'age', 18)
print(getattr(sobj, 'age'))
delattr(sobj, 'age')
# print(getattr(sobj, 'age'))
print(hasattr(sobj, 'age'))
print(hasattr(sobj, 'name'))