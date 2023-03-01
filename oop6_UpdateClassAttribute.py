#crud create read update delete
#manual, built in
#class method   // outside hold object

class MyClass:
    def __init__(self):
        self.name = "WinHtut"
        self.age = 25
        self.hobby = "Hacking"
    def update(self):
        self.name = "Vijja"
        self.age = 26
        self.hobby = "research"
o1 = MyClass()
o2 = MyClass()
print("Before Update")
print(o1.name, o1.age, o1.hobby)
print(o2.name, o2.age, o2.hobby)
# o1.name = "hnin"
# o1.age = 27
# o1.hobby = "programming"
o1.update()
o2.update()
# o1.name = "snow"
# o1.age = 20
# o1.hobby = "scientist"
print("After upate manually")
print(o1.name, o1.age, o1.hobby)
print(o2.name, o2.age, o2.hobby)