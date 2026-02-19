from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
    def refund(self, amount):
        print(f"Refunded ₹{amount} to Credit Card.")

class UPIPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

cc = CreditCardPayment()
cc.pay(1000)
cc.refund(500)
print()
upi = UPIPayment()