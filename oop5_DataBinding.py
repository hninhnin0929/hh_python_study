class MyClass:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2
    def mInfo(self):
        print("from mInfo => ", self.cat1, ":", self.cat2)

obj = MyClass('apple', 'orange')
print("obj data: ", obj.cat1, ' ', obj.cat2)
obj.mInfo()