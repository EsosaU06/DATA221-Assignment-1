def timeFromSecondsSinceMidnight(amountInSeconds):
    if amountInSeconds < 0: # check if a valid amount of seconds was given
        return ("Invalid input, seconds cannot be less than zero.")
    
    # create all the variables and their default values
    amountInMinutes = 0
    amOrPm = "AM"
    amountInHours = 0
    amountInDays = 0
    
    # check how many minutes are in the given seconds... 
    while amountInSeconds >= 60:
        amountInMinutes += 1
        amountInSeconds -= 60
    
    # ...then the amount of hours that are in the given minutes
    while amountInMinutes >= 60:
        amountInHours += 1
        amountInMinutes -= 60

    # check if the hours exceed 24, if so,
    # in order to prevent AM/PM errors, account for the full days
    # (this wont be returned)
    while amountInHours >= 24:
        amountInDays +=1
        amountInHours -= 24
    
    if amountInHours >= 12: # without the previous logic for days, this if statement would cause errors
        amOrPm = "PM"
    
    return(f"{amountInHours} {amountInMinutes} {amountInSeconds} {amOrPm}")
        
# example code:
# print(timeFromSecondsSinceMidnight(26500))
