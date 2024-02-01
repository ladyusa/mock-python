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
    
    def add_interest(self, rate):
        self.balance = self.balance + (self.balance * rate)

class Bank:

    def __init__(self, name):
        self.name = name
        self.accounts = dict()

    def add_account(self, account):
        self.accounts[account.get_name()] = account

    def transfer(self, from_act, to_act, amount):
        self.accounts[from_act].withdraw(amount)
        self.accounts[to_act].deposit(amount)

    def give_interest_all(self, rate):
        for name in self.accounts:
            self.accounts[name].add_interest(rate)

if __name__ == '__main__':
    usa = BankAccount("Usa", 1000)
    chakrit = BankAccount("Chakrit", 2000)

    bankKU = Bank("KU")

    bankKU.add_account(usa)
    bankKU.add_account(chakrit)

    print("Usa's balance:", usa.balance)
    print("Chakrit's balance:", chakrit.balance)

    bankKU.transfer("Chakrit", "Usa", 100)

    print("Usa's balance:", usa.balance)
    print("Chakrit's balance:", chakrit.balance)
