#OOP
#Inheritance => Class B can use the attributes of Class A
#Data Abstraction
#Encapsulation
#Polymorphism

#multiple inheritancee

# class ClassA:
#     def someMethod():
#         pass
# class ClassB(ClassA):
#     pass

class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dObj = Dog()
dObj.bark()
dObj.eat()

class Parent:
    def own(self):
        print("Wee havee man jaweels")
class Child(Parent):
    def poor(self):
        print("so so poor")
cObj = Child()
cObj.poor()
cObj.own()