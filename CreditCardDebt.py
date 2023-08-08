#Function that calculates the Total Monthly Ineterest
def CalculateInterest(Bal,APR):
    DailyPercentageRate=APR/365 #The Daily Interest Rate
    DailyInterestCharge=(DailyPercentageRate/100)*Bal #The Daily Interest Charge
    MonthlyInterest=DailyInterestCharge*30 #The total interest that needs to be paid on the next statement. 
    return MonthlyInterest

# Input Information from Debter 
BalancePastDue=input("What is your overdue balance on your credit card ?: ")
APR=input("What is the Annual Percentage Rate (APR) of your credit card ?: ")

TotalMonthlyInterest=CalculateInterest(float(BalancePastDue),float(APR))
print(TotalMonthlyInterest)

    
