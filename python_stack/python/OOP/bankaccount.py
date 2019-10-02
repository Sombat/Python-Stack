# Assignment: BankAccount
# Objectives
# Practice writing classes

class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.interest_rate = int_rate
        self.account_balance = balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Interest Rate: {self.interest_rate}, Balance: ${self.account_balance}")
        return self
    
    def yield_interest(self):
        print(f"Interest: {self.account_balance*self.interest_rate}")
        return self
        
Account1 = BankAccount()
Account1.deposit(100) .deposit(200) .deposit(220) .withdraw(20) .yield_interest() .display_account_info()

Account2 = BankAccount()
Account2.deposit(51) .deposit(49) .withdraw(1) .withdraw(1) .withdraw(1) .withdraw(1) .yield_interest() .display_account_info()