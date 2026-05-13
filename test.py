from main import Account, SavingsAccount, CheckingAccount

if __name__ == "__main__":
    savings = SavingsAccount("Andre", 1000, 0.02)
    savings.deposit(500)
    savings.apply_interest()
    print(savings.get_balance())

    checking = CheckingAccount("TestUser", 3000)
    checking.withdraw(3500)
    print(checking.get_balance())
