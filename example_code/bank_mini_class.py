class BankAccount:
    """ create a bank account """

    def __init__(self, name, balance, isClient=False):
        self.name = name
        self.balance = balance
        self.isClient = isClient

    def client(self):
        """ client information """
        return f'Account name: {self.name}, balance: {self.balance}'

    def commission(self, isClient):
        """ charge commision """
        if isClient:
            return 2.5
        else:
            return 5
