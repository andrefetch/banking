class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > self.balance:
            raise Exception(f"{self.balance} is less than {amount}")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception(f"Can't withdraw {amount} because it's more than {self.balance}")