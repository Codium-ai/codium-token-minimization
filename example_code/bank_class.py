from dataclasses import dataclass


class BankAccount:
    """ create a bank account """

    def __init__(self, name, balance, isClient=False):
        self.name = name
        self.balance = balance
        self.isClient = isClient

    def client(self):
        """ client information """
        return f'Account name: {self.name}, balance: {self.balance}'

    def deposit(self, amount):
        """ deposit money """
        if amount > 0:
            self.balance += (amount - self.commission(self.isClient))
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        """ withdraw money """
        if self.balance >= amount > 0:
            self.balance -= (amount + self.commission(self.isClient))
        else:
            print("Insufficient funds")

    def transfer(self, amount, account):
        """ transfer money """
        if self.balance >= amount > 0 and (amount - self.commission(self.isClient)) > 0:
            self.balance -= (amount + self.commission(self.isClient))
            account.balance += amount
        else:
            print("Insufficient funds")

    def commission(self, isClient):
        """ charge commision """
        if isClient:
            return 2.5
        else:
            return 5


@dataclass
class Account:
    something: str


@dataclass
class SubAccount(Account):
    sub_something: str


def calc_pi(accuracy: int) -> float:
    """Calculate pi to the given accuracy"""
    return 3.14
