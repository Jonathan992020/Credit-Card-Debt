# A function that converts the weight specified 
def ConvertUnit(weight,unit):
    if unit=="k":
        ConvertedWeight=float(weight)*2.20462
    elif unit=="l":
        ConvertedWeight=float(weight)/2.20462
    else:
        # Throw the following error message. 
        print("The unit you specified is wrong")

    return ConvertedWeight

# This program asks for your weight 
Weight=input("What is your current weight ?: ") # Prompt User for weight. 
Unit=input("In K(g) or L(bs) ?: ")  #Prompt User for the Units of the weight. 
print(ConvertUnit(Weight,Unit))
