def CalculateXToThePowerOfY(listInput):
    validList = []
    # creating the list to put the
    # valid x-y pairs in
    
    for pair in listInput:
        baseX = pair[0]
        # the first index is the base, x
        
        powerY = pair[1]
        # the second index is the exponent, y
        
        if powerY >= 0:
            result = pow(baseX, powerY)
            validList.append(result)
            # only add the pairs to the list if
            # the exponent is not negative
            
    # once the loop ends (every pair
    # has been iterated through) print
    # the results
    print(validList)