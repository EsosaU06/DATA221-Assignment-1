def ListDistributionAnalysis(listInput=None):
    if listInput is None:
        # check if a list was given
        return None
    
    amountOfNumbersInList = len(listInput)
    # used when computing the percentage
    
    uniqueValueDictionary = {} # creating a dictionary to store the unique values
    
    for number in listInput:
        if number not in uniqueValueDictionary:
            uniqueValueDictionary[number] = 0
            # adding the unique number to the dictionary, if it wasn't already there
    
    for key in uniqueValueDictionary:
        amountLessOrGreater = 0
        
        for number in listInput:
            if number <= key:
                amountLessOrGreater += 1
                
        amountLessOrGreaterPercentage = (amountLessOrGreater / amountOfNumbersInList) * 100
        uniqueValueDictionary[key] = amountLessOrGreaterPercentage
    
    # "The resulting dictioary should be sorted by key before being returned":
    
    sortedUniqueValueDictionary = dict(sorted(uniqueValueDictionary.items()))
    # this line turns the dict into a tuple (so the sorted function can be used)
    # and then back into a dictionary
    
    return sortedUniqueValueDictionary

# example code
# numbers = [5,1,2,3,1,2,2,2,3,3,5,5,0]
# print(ListDistributionAnalysis(numbers))