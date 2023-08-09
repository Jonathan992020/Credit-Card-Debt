#Function that calculates the Total Monthly Ineterest
def CalculateInterest(Bal,APR):
    DailyPercentageRate=APR/365 #The Daily Interest Rate
    DailyInterestCharge=(DailyPercentageRate/100)*Bal #The Daily Interest Charge
    MonthlyInterest=DailyInterestCharge*30 #The total interest that needs to be paid on the next statement. 
    return MonthlyInterest

#Function that calculates the new balance 
def NewBal(Interest):
    newbal=float(BalancePastDue)+Interest
    return newbal

def InDebt(Payment):
    InDebt=float(Payment)-newbalance
    if InDebt < 0:
        return True
    else:
        return False

# Input Information from Debter 
BalancePastDue=input("What is your overdue balance on your credit card ?: ")
APR=input("What is the Annual Percentage Rate (APR) of your credit card ?: ")

# Output
TotalMonthlyInterest=CalculateInterest(float(BalancePastDue),float(APR))
print(TotalMonthlyInterest)     # Print the Interest Charged. 
newbalance=NewBal(TotalMonthlyInterest)
print(newbalance) # Print the Updated Balance.

# PAYMENTS
Payment=input("How much will you contribute towards paying off the balance ?: ")
print(InDebt(Payment)) # Returns True if we are in debt and False if we are not in debt. 

