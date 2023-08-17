# This function finds the maximum number in a list 
def findmax(list_of_numbers):
    maximum=list_of_numbers[0]  # Set the maximum to the first element in the list.  
    
    for i in list_of_numbers:
        if i>maximum:
            maximum=i
        
    return maximum

# This function finds the minimum number in a list 
def findmin(list_of_numbers):
    minimum=list_of_numbers[0]

    for i in list_of_numbers:
        if i<minimum:
            minimum=i
    
    return minimum
