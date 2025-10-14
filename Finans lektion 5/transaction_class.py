class Transaction():

    def __init__(self, type, amount, category, desc=None, date="1999-12-12"):
        self.type = type
        self.amount = amount
        self.category =category
        self.decs = desc
        self.date = date
    def __str__(self):
        if self.type == "e":
            sign = "-"
        else:
            sign = ""
        return f"{self.date}: {self.category}: {sign} {self.amount}kr"
    
transaction = Transaction("e","500", "rent")
print(transaction)