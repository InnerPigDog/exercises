import threading


class BankAccount:
    def __init__(self):
        self.acc_open = False
        self.balance = 0

    def get_balance(self):
        if self.acc_open:
            return self.balance
        else:
            raise ValueError("Account is closed.")

    def open(self):
        if self.acc_open:
            raise ValueError("Account is already open.")
        self.acc_open = True

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        if self.acc_open:
            self.balance += amount
        else:
            raise ValueError("Account is closed.")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")
        if self.balance - amount < 0:
            raise ValueError("Balance cannot be negative.")
        if self.acc_open:
            self.balance -= amount
        else:
            raise ValueError("Account is closed.")

    def close(self):
        if not self.acc_open:
            raise ValueError("Account is already closed.")
        self.acc_open = False
        self.balance = 0
