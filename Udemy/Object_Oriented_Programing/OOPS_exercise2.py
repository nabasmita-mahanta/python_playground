# Object Oriented Programming Challenge
# For this challenge, create a bank account class that has two attributes:
# owner
# balance
#
# and two methods:
# deposit
# withdraw

# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals,
# and test to make sure the account can't be overdrawn.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: {self.balance}'

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print("Deposit Accepted")

    def withdraw(self, amount):
        if amount<0:
            print("Only positive amount is accepted")
        elif self.balance < amount:
            print("Funds Unavailable!")
        else:
            self.balance = self.balance - amount
            print("Withdrawal Accepted")


# 1. Instantiate the class

acc1 = Account("Jose", 100)

# 2. Print the object
print(acc1)

# 3. Show the account owner attribute
print(acc1.owner)

# 4. Show the account balance attribute
print(acc1.balance)

# 5. Make a series of deposits and withdrawals
acc1.deposit(500)
acc1.deposit(-500)
acc1.deposit(700)
acc1.withdraw(800)
acc1.withdraw(2000)
print(acc1.balance)
acc1.withdraw(-5000)
acc1.withdraw("qwer")
print(acc1.balance)
