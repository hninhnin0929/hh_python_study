class Price():
    def payment(self):
        print("From Parent Class")

class Child(Price):
    def payment(self):
        # return super().payment()
        print("From Child Class")
class GrandChild(Child):
    def payment(self):
        print("From GrandChildClass")
           
obj = GrandChild()
obj1 = Child()
obj1.payment()
obj.payment()
#overrie
#abstraction မသိစေချင်တဲ့အရာ ဖုံးအုပ်ထားတဲ့အရာ
