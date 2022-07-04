

def calculate_loan():
    age = int(input("age: "))
    amount = float(input("Amount requested: "))
    interest = float(input("Interest rate: "))
    loan_time_month = float(input("Loan time in months: "))
    if age >18 :
        loan_time_year = loan_time_month/12
        rate_owed = (interest*amount)/100
        amount_repaid = amount +rate_owed
        compound_interest = amount * (1 + interest/100)**loan_time_year
        print (f"You will owe {compound_interest}")
    else:
        print("We do not give loans to children")




calculate_loan()
