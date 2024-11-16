from abc import ABC, abstractmethod

# Abstract Base Class for Payment Method
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# NetBanking Payment Implementation
class NetBanking(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using NetBanking.")

# Cash Payment Implementation
class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash.")

# Card Payment Implementation
class Card(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Card.")

# UPI Payment Implementation
class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

# Function to process payment
def process_payment(payment_method, amount):
    if not isinstance(payment_method, PaymentMethod):
        raise TypeError("Invalid payment method!")
    payment_method.pay(amount)

# Usage Example
if __name__ == "__main__":
    amount = 500
    
    # Use NetBanking
    payment_method = NetBanking()
    process_payment(payment_method, amount)
    
    # Use Cash
    payment_method = Cash()
    process_payment(payment_method, amount)
    
    # Use Card
    payment_method = Card()
    process_payment(payment_method, amount)
    
    # Use UPI
    payment_method = UPI()
    process_payment(payment_method, amount)
