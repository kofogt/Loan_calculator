

def calculate_loan():
    age = int(input("age: "))
    amount = float(input("Amount requested: "))
    interest = float(input("Interest rate: "))
    if age >18 :
        rate_owed = (interest*amount)/100
        amount_repaid = amount +rate_owed
        print (f"You will owe {amount_repaid}")
    else:
        print("We do not give loans to children")




calculate_loan()
