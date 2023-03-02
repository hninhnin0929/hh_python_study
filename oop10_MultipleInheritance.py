class Animal:
    color = "yellow"
    age = 2
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
odog = Dog()
odog.age = 5
odog.color = "black"
print(odog.color)
print(odog.age)

class Parent:
    def parent(self):
        print("This is form parent")
class Aunty:
    def aunty(self):
        print("This is form Aunty")
class Uncle:
    def uncle(self):
        print("This is form Uncle")

class Child(Parent, Aunty, Uncle):
    def child(self):
        print("This is from child")
obj = Child()
obj.aunty()
obj.parent()
obj.uncle()
#-------------------------------------------------
class Parent:
    def parent(self):
        print("This is form parent")
class Aunty(Parent):
    def aunty(self):
        print("This is form Aunty")
class Uncle:
    def uncle(self):
        print("This is form Uncle")

class Child(Aunty):
    def child(self):
        print("This is from child")
obj1 = Child()
obj1.aunty()
obj1.parent()
#------------------------------------------
class Base1:
    def multi(self, a, b):
        return a*b
class Base2(Base1):
    def Adding(self, a, b):
        return a+b
class Derived(Base2):
    def sub(self, a,b):
        return a-b
obj2 = Derived()
print("From Base 1", obj2.multi(5,5))
print("From Base 2", obj2.Adding(5,5))
print("From Derived", obj2.sub(10,5))


