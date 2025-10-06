class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Otillräckligt saldo")
        else:
            self.balance -= amount

    def show_balance(self):
       print(f"Current balance for {self.owner}: {self.balance}")


    def transfer(self, amount, owner, balance)
        
    def __str__(self):
        return f"Balance is {self.balance}"
    

b1 = BankAccount("Bert")
b2 = BankAccount("Mona")
banklista = [b1,b2]



