

def calculate_loan():
    age = int(input("age: "))
    amount = float(input("Amount requested: "))
    interest = float(input("Interest rate: "))
    loan_time_month = float(input("Loan time in months: "))
    if age >18 :
        loan_time_year = loan_time_month/12
        compound_interest = amount * (1 + interest/100)**loan_time_year
        print (f"You will owe {compound_interest}")
    else:
        print("We do not give loans to children")


# calculate_loan()

#How long it will take to pay off a loan

def loan_repayment():
    amount = float(input("How much do you owe: "))
    monthly_repayment = float(input("How much do you wish to pay monthly: "))
    interest = float(input("What is your interest rate per annum: "))
    monthly_interest = (interest / 100) / 12
    balance =amount
    count = 0
    while balance > 0:
        count +=1
        plus_interest = balance + (balance *monthly_interest)
        less_repayment = plus_interest - monthly_repayment
        balance=less_repayment

    print(count)
loan_repayment()