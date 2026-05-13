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
        self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def get_owner(self):
        return self.owner
    
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def apply_interest(self):
        self.interest_rate += (self.interest_rate * 0.25)
        self.balance += self.interest_rate

class CheckingAccount(Account):
    def __init__(self, owner, balance, over_draft_limit=1000):
        super().__init__(owner, balance)

        self.over_draft_limit = over_draft_limit
    
    def get_overdraft(self):
        return self.over_draft_limit
    
    def withdraw(self, amount):
        if amount > self.over_draft_limit:
            raise Exception(f"Can't withdraw the amount: {amount} because it's over the overdraft limit of: ${self.get_overdraft()}")
        self.balance -= amount