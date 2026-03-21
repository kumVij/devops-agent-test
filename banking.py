"""
banking.py — Simple banking system
Has 3 intentional bugs for agent testing:
  Bug 1: calculate_interest divides instead of multiplies
  Bug 2: transfer_funds doesn't check for negative amount
  Bug 3: get_balance returns wrong type (str instead of float)
"""


class BankAccount:
    def __init__(self, account_id: str, owner: str, balance: float = 0.0):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.transactions = []

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append({"type": "withdrawal", "amount": amount})
        return self.balance

    def get_balance(self) -> float:
        # BUG 1: returns string instead of float
        return str(self.balance)

    def calculate_interest(self, rate: float, years: int) -> float:
        # BUG 2: divides instead of multiplies
        # correct: self.balance * rate * years
        # wrong:   self.balance / rate / years
        return self.balance / rate / years

    def transfer_funds(self, target: "BankAccount", amount: float) -> bool:
        # BUG 3: missing negative amount check
        # should raise ValueError if amount <= 0
        if amount > self.balance:
            raise ValueError("Insufficient funds for transfer")
        self.balance -= amount
        target.balance += amount
        self.transactions.append({"type": "transfer_out", "amount": amount})
        target.transactions.append({"type": "transfer_in", "amount": amount})
        return True

    def get_statement(self) -> list:
        return self.transactions.copy()