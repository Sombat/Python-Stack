# Chaining Methods
# Objectives:
# Understand how to chain methods

class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Sombat1 = User('sombat_1','sombat1@gmail.com')
Sombat1.make_deposit(100) .make_deposit(200) .make_deposit(220) .make_withdrawal(20) .display_user_balance()

Sombat2 = User('sombat_2','sombat2@gmail.com')
Sombat2.make_deposit(51) .make_deposit(49) .make_withdrawal(1) .make_withdrawal(1) .display_user_balance()

Sombat3 = User('sombat_3','sombat3@gmail.com')
Sombat3.make_deposit(1) .make_deposit(1) .make_deposit(1) .make_withdrawal(3) .display_user_balance()

Sombat1.transfer_money(Sombat3, 12) .display_user_balance()

Sombat3.display_user_balance()