from random import random

def sortRandomListOfValues(listOfValues, x):
    greaterOrEqualToXList = []
    # the list of values that are greater than or
    # equal to x - the randomized number set
    
    listOfValues.sort()
    # the function that sorts the list
    
    for value in listOfValues:
        if value >= x:
            # checking if the value is greater than or equal to x
            greaterOrEqualToXList.append(value)
            # if it is, it is added to the list
    
    # The print statements:
    print(f"Sorted List:\n{listOfValues}", end="\n\n")
    
    # adding a double space between inputs to improve readability
    print(f"x = {x}", end="\n\n")
    
    
    if len(greaterOrEqualToXList)>0:
        # this if statement checks
        # if there are any numbers that are
        # greater than or equal to x
        
        print(f"The first value in the list that is greater than or equal to x is {greaterOrEqualToXList[0]}.")
        # greaterOrEqualToXList[0] -> The first value the program found that is greater than or equal to x

# i decided to keep the starter code in

values = [random() for i in range(20)]
x = random()

sortRandomListOfValues(values, x)