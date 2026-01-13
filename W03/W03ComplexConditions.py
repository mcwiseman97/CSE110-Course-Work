"""
Author: Michael Wiseman 
Assignment: Loan Approval
Date: 1/8/26
"""
# Boolean expression  =  True or False

# order of operations are Not operators, then And, and Or is laste



#Qualifying for a loan


# Determine persons qualification

print("For the following questions, please answer with a rating between 1 - 10:")

loan_size = int(input("How large is the loan? "))

credit_history = int(input("How good is your credit history? "))

income = int(input("How high is your income? "))

down_payment = int(input("How large is your down payment? "))

approval_status = False


if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        approval_status = True
    elif credit_history >= 7 or income >= 7:    
        if down_payment >= 5:
            approval_status = True     
        else:
            approval_status = False
    else:
        approval_status = False
else:
    if credit_history < 4:
        approval_status = False
    else:
        if income >= 7 or down_payment >= 7:
            approval_status = True
        elif income >= 4 and down_payment >= 4:
            approval_status = True
        else:
            approval_status = False

if approval_status:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")
    
