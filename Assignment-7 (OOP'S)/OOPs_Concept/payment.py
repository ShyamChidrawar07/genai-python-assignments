from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        if amount > 0:
            print(f"Processing credit card payment of {amount}")
        else:
            print("Invalid payment amount")

class UPIPayment(Payment):
    def process_payment(self, amount):
        if amount > 0:
            print(f"Processing UPI payment of {amount}")
        else:
            print("Invalid payment amount")

creditcard=CreditCardPayment()
upi=UPIPayment()
creditcard.process_payment(1000)
upi.process_payment(500)
creditcard.process_payment(-100)
upi.process_payment(-500)