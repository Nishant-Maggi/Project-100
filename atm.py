class Atm(object):
    def __init__(self, card_number, pin_number, name_of_user, balance):
        self.card_number = card_number
        self.pin_number = pin_number
        self.name_of_user = name_of_user
        self.balance = balance

    def cashWithdrawal(self, amount):
        print("Transaction of " + amount + " successful \n card number: " + self.card_number + "\n pin number: " + self.pin_number)

    def balance_enquiry(self, balance):
        print("The balance remaining is " + self.balance)


atm1 = Atm("1234567*XXX@", "76**1", "Nishant", "1500")
atm1.cashWithdrawal("$500")
atm1.balance_enquiry("$1500")