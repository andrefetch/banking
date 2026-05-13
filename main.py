class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise Exception(f"Can't withdraw {amount} because it's more than {self._balance}")
        self._balance -= amount

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self.owner

    def __repr__(self):
        return f"Account({self.owner}, ${self._balance})"

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

class CheckingAccount(Account):
    def __init__(self, owner, balance, overdraft_limit=1000):
        super().__init__(owner, balance)

        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            raise Exception(f"Can't withdraw the amount: {amount} because it's over the overdraft limit of: ${self.overdraft_limit}")
        self._balance -= amount