import random
import datetime

# A Credit Card Object Blueprint class
class CreditCard:
    def digitnumber(self):
        Primary_Account_number=random.randrange(10**15,10**16)
        return Primary_Account_number

    def expiration(self):
        current_date=datetime.date.today() #Retrieve the current date
        timedelta=datetime.timedelta(days=1) #Represents a time difference of 1 year. 
        expiration_date=current_date+(365*5*timedelta)  #The expiration date.
        return expiration_date 

    def cardverificationvalue(self):
        CVV=random.randrange(100,999)   # A 3 digit verification number.
        return CVV 
        

# Creating a Credit Card Object 
TD_Cashback_Visa_Card=CreditCard() 
TD_Cashback_Visa_Card.PrimaryCardNumber=TD_Cashback_Visa_Card.digitnumber()
TD_Cashback_Visa_Card.ExpirationDate=TD_Cashback_Visa_Card.expiration()
TD_Cashback_Visa_Card.CardVerificationValue=TD_Cashback_Visa_Card.cardverificationvalue()


print("Your TD Cash back visa card has a primary card number of "+str(TD_Cashback_Visa_Card.PrimaryCardNumber)+
      " with the experation date being "+str(TD_Cashback_Visa_Card.ExpirationDate)+" and the card verification value is "+str(TD_Cashback_Visa_Card.CardVerificationValue))
