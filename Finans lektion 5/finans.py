import datetime
from transaction_class import Transaction
#Date formant

test_transactions = ["income", "5000", "salery", "test dec", "2004-20-02"]
new_transaction = []
new_transaction.append(new_transaction)

def add_transaction(transaction):
    transaction.append(transaction)
    print(f"added trans {transaction}")
    
def show_finans():
    balance = 0
    for transaction in transactions:
        transaction_type = transaction[0]
        amount = transaction[1]
        if transaction_type == "i":
            balance += amount
        else:
            balance -= amount
    return balance

    
def create_budget():
    pass
def show_budget():
    pass
def start_monetoring():
    pass
def read_finans_from_datafile():
    pass
def write_fianns_to_datafile():
    pass
def show_main_menu():
    print("Wow")

def main():
    while True:
        show_main_menu()
        valid_input = False
        while not valid_input:
            menu_choice = input("1-6")
            match menu_choice:
                case "1":
                    transaction_type = input("Type of trans(I or E: )")
                    amount = input("Transaction amout (kr): ")
                    category = input("Category (Food/Transport/Salery/Rent): ").lower()
                    description = input("Optional desc")
                    date = input ("optional date for trans:")
                    new_transaction = Transaction(transaction_type, amount, category, description, date) 
                    add_transaction(new_transaction)
                    valid_input = True
                case "2":
                    show_finans() #lägg till break efter valid_input alla case för de inte ska kolla igenom alla andra 
                case "3":
                    create_budget()
                case "4":
                    show_budget()
                case "5":
                    start_monetoring()
                    quit()
                case _: # eller case default 
                    print("wrong input")

main()