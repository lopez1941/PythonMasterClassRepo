# convention is to start classes with Upper case letter and camel case them
import datetime
import pytz

class Account:
    """ Simple account class with balance """
    # first method called is 'new'. init method then updates
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print("Account created for " + self.name)
        self.transaction_list = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # appending date/time to transaction_list. localizing utc time using pytz
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("The amount must be greater than 0 and no greater than account balance.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {0}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))

if __name__ == '__main__':
    donnie = Account("Donnie", 0)
    donnie.deposit(1000)
    donnie.withdrawal(5000)
    donnie.withdrawal(50)
    donnie.show_transactions()
