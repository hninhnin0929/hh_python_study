class MyClass:
    pass

obj1 = MyClass()
obj2 = MyClass()

obj1.x = 5
obj1.y = 10
obj2.x = 15
obj2.y = 20
print('obj1 x:{0} : y:{1}'.format(obj1.x, obj1.y))
print('obj2 x:{0} : y:{1}'.format(obj2.x, obj2.y))
# --------------------------------------------

class MyClass1:
    def myMethod(self): #normal method
        self.x = 10
        self.y = 20

obj1 = MyClass1()
obj2 = MyClass1()
obj1.myMethod() #must be initialized #switch button
print(obj1.x, obj1.y)
obj2.myMethod()
print(obj2.x, obj2.y)