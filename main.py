"""
# Student loan calculator
M = L[i(1+i)n] / [(1+i)n-1]
- M = monthly payment
- L = Loan amount
- i = interest rate (for an interest rate of 5%, i = 0.05)
- n = number of payments
"""

#Declare variables
monthly_payment = 0 
loan_amount = 0
interest_rate = 0
number_of_payments = 0
loanduration_in_years = 0
#payments
loan_amount = input("How much money will you borrow? ")

interest_rate = input("What is the interest rate on the loan? ")

loanduration_in_years = input("How many years will it take you to pay off the loan? ")

#Convert the strings into floating numbers so we can use them in the  formula
loanduration_in_years = float(loanduration_in_years)
loan_amount = float(loan_amount)
interest_rate = float(interest_rate)

#Since payments are once per month, number of payments is number of years for the loan

number_of_payments = loanduration_in_years * 12

#calculate the monthly payment based on the formula

monthly_payment = loan_amount * interest_rate * (1 + interest_rate) * number_of_payments / ((1 + interest_rate) * number_of_payments - 1)

#Result to the program

print("Your monthly payment will be " + str(monthly_payment))