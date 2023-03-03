#encapsulation
#public
#private    => __variable or method (double underscore)
#protected  => _variable or method (single underscore)

class Parent: #base class
    def __init__(self,age) -> None:
        self._age = age #don't touch from the outside
class Sub(Parent):
    def getData(self):
        print(self._age)

obj = Sub(100)
obj.getData()
