import math 

# tapes of calculators
print("Types of calculations:") 
print() 
print("Investment - to calculate the amount of interest you'll earn on your investment") 
print("Bond - to calculate the amount you'll have to pay on a home loan") 
print() 

# possible outputs
calculator = input("Please enter either 'Investment' or 'Bond' from the menu above: ").lower()
output1 = "bond"
output2 = "investment"

# investment calculator
if calculator == output2:
    # amount that user deposits 
    principal_amount = int(input("How much money would you like to deposit (in GBP)? ")) 
    # interest entered by user  
    input_interest = int(input("Please enter the annual interest rate (in %)? ")) / 100
    # number of years that money is being invested 
    investment_length = int(input("Please enter length of investment (in years)? ")) 
    # total amount once interest has been applied  
    interest_type=input("Would you like to check 'simple' or 'compound' interest on your investment? ").lower()
    
    interest1 = "simple" 
    interest2 = "compound" 

    # simple interest calculator
    simple = principal_amount * (1 + input_interest*investment_length) 
    # compound interest calculator
    compound = principal_amount * math.pow((1 + input_interest), investment_length)

    if interest_type == interest1: 
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Deposit: {principal_amount:18} GBP\
                  \nInterest rate: {input_interest*100:11} %\
                  \nLength of investment: {investment_length:3} years\
                  \nInterest amount: {simple - principal_amount:12} GBP")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Total amount of your investment including simple interest: ", simple, "GBP") 
        print()

    elif interest_type == interest2: 
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Deposit: {principal_amount:18} GBP\
                  \nInterest rate: {input_interest*100:11} %\
                  \nLenght of investment: {investment_length:3} years\
                  \nInterest amount: {round(compound - principal_amount, 2):13} GBP")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Total amount of your investment including compound interest: " , round(compound, 2), "GBP") 
        print()

# bond calculator
elif calculator == output1: 
    # present value of the house 
    house_value = int(input("What is the current value of the property (in GBP)? "))
    # interest rate 
    interest_rate_bond = int(input("Please enter the current interest rate (in %) ")) / 100
    # number of months they plan to take to repay the bond 
    bond_length = int(input("Please enter number of repayments (in months) "))
    
    # monthly interest rate, calculated by dividing the annual interest rate by 12 
    monthly_interest_rate = interest_rate_bond / 12

    bond_repayment = (monthly_interest_rate * house_value)/(1 - (1 + monthly_interest_rate)**(-bond_length))
                                                         
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Value of the property:   {house_value} GBP\
              \nInterest rate: {interest_rate_bond*100:13} %\
              \nLength of the bond: {bond_length:7} months\
              \nMonthly repayment: {round(bond_repayment,2):13} GBP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

else:                         
    print("Please try again")
