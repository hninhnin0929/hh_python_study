class Parent: #base class
    def __init__(self, age) -> None:
        self.__age = age

# p = Parent(30)
# print(p.__dict__)
# print(p.__age) # cannot access age like this
class Child(Parent):
    def modify(self, input):
        self.__age = input
        return self.__age
    def getData(self):
        self.__age = 30
        print(self.__age)
obj = Child(10)
print(obj.__dict__)
print(obj.modify(20))
print(obj.__dict__)
obj.getData()

#----------------------------------
class Animal:
    def __init__(self, name, color, age, behavior) -> None:
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior
class Dog(Animal):
    def dogModify(self, name, color, age, behavior):
        self.__name = name
        self.__color = color
        self.__age = age
        self.__behavior = behavior
    def dogGetData(self):
        print(self.__name,self.__color,self.__age,self.__behavior )

obj = Dog("mimi","yellow",3,"eat")
print(obj.__dict__)
# print(obj.dogGetData())
obj.dogModify("super", "red", 5, "fly")
print(obj.__dict__)
obj.dogGetData()