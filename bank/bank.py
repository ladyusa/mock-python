class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = dict()

    def add_account(self, account):
        self.accounts[account.get_name()] = account

    def transfer(self, from_act, to_act, amount):
        self.accounts[from_act].withdraw(amount)
        self.accounts[to_act].deposit(amount)
