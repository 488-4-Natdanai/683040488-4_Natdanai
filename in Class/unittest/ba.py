# bank_account.py
class BankAccount:
    def __init__(self, initial_balance=0):
        # Bug 1: Doesn't validate if initial_balance is negative
        if initial_balance < 0 :
            raise ValueError("initial balance cannot be negative")
        self.balance = initial_balance
        self.is_open = True

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError("Cannot deposit to a closed account")
        # Bug 2: Missing validation for positive amount
        if amount <= 0: 
            raise ValueError(...)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError("Cannot withdraw from a closed account")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        # Bug 3: No check for sufficient funds
        # Should have: 
        if amount > self.balance: 
            raise ValueError("bug3")
        self.balance -= amount
        return self.balance

    def close(self):
        # Bug 4: Doesn't reset balance to zero when closing account
        self.balance = 0
        self.is_open = False