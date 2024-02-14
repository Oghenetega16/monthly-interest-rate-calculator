def main():
    print("This is a monthly payment loan calculator.")
    print()
    
    principal = float(input("Input the loan amount: "))
    rate = float(input("Input the annual interest rate: "))
    years = int(input("Input the year: "))
    
    monthly_interest_rate = rate / 1200
    number_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))
    
    print("The monthly payment for this loan is: %.2f" % monthly_payment)
    
    
main()