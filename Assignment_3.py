
class Payment:
    def pay(self, amount):
        pass


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")


class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")


class PayPal(Payment):
    def pay(self, amount):
        print("Paid", amount, "using PayPal")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        self.strategy.pay(amount)


p1 = PaymentProcessor(CreditCard())
p1.process_payment(1000)

p2 = PaymentProcessor(UPI())
p2.process_payment(500)

p3 = PaymentProcessor(PayPal())
p3.process_payment(1500)
