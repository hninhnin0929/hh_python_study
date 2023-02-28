class MyClass:
    def __init__(self, xAxis, yAxis):   #special method
        self.xAxis = xAxis  #dot notation
        self.yAxis = yAxis
obj1 = MyClass(10, 20)
print("for obj1=> ",obj1.xAxis, obj1.yAxis)
obj2 = MyClass(1.1, 2.2)
print("for obj2=> ",obj2.xAxis, obj2.yAxis)