class BankAccount:
    def __init__(self):
        self.__balance = 0

    def set_balance(self,balance):
        self.__balance = balance

    def make_deposit(self,deposit):
        self.__balance += deposit

    def make_withdraw(self,withdraw):
        if withdraw <= self.__balance:
            self.__balance -= withdraw
        else:
            print("Insufficient balance")

    def checkbalance(self):
        return self.__balance
        

obj = BankAccount()
obj.set_balance(12000)
obj.make_deposit(1300)
obj.make_withdraw(12000)
print(obj.checkbalance())
