from re import S


class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name;
        self.payment = payment;
        self.amount = amount;
   
    def pay(self):
        self.payment = 'yes'

    def status(self):
        if self.payment =='yes':
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + ' is not paid yet'

nathan = Payslips('Nathan', "no", 1000);
roger = Payslips('Roger', "no", 3000);

print(nathan.status())
print("\n")
print(nathan.status())

##We're modifying self.payment in the Nathan instance. Roger is not affected.
nathan.pay();

print('After payment');

print(nathan.status())
print("\n")
print(nathan.status())