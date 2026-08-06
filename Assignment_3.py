class PaymentStrategy:
    def pay(self, amount):
        print("No payment method selected")

class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print("Paid", amount, "using Credit Card:", self.card_number)


class UpiPayment(PaymentStrategy):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("Paid", amount, "using UPI ID:", self.upi_id)


class CashOnDelivery(PaymentStrategy):
    def pay(self, amount):
        print("Rs.", amount, "will be paid on delivery (Cash)")

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

amount = 1500

payment = PaymentContext(CreditCardPayment("1234567890123456"))
payment.make_payment(amount)

payment.set_strategy(UpiPayment("student@upi"))
payment.make_payment(amount)

payment.set_strategy(CashOnDelivery())
payment.make_payment(amount)