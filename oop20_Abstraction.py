from abc import ABC, abstractmethod

class Price(ABC):
    def print_slip(self, amount):
        print("Payment amount $", amount)
    @abstractmethod
    def payment(self, amount):
        print("This is important from abstract class")
        return "nothing from abstract method"


class CreditCardPayment(Price):
    def payment(self, amount):
        print("Payment with Credit Card $", amount) 
class MobileBanking(Price):
    def payment(self, amount):
        super().payment(amount)
        print("Payment with Mobile Banking $", amount)

obj = CreditCardPayment()
obj.print_slip(1000)
obj.payment(1000)
obj1 = MobileBanking()
obj1.print_slip(2000)
obj1.payment(2000)
