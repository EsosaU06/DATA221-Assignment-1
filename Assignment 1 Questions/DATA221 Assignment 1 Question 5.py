import math

def AreaCoveredBySmallerCircle(radiusOfFirstCircle, radiusOfSecondCircle):
    try:
        if not (radiusOfFirstCircle > 0 and radiusOfSecondCircle > 0 ):
            # early return in case either radii are negative,
            # assuming zero is not counted as a positive integer
            return ("Invalid input, at least one radius given is negative.")
        
        areaOfFirstCircle = (math.pi)*(pow(radiusOfFirstCircle, 2)) 
        areaOfSecondCircle = (math.pi)*(pow(radiusOfSecondCircle, 2))
        # we do the (pi * r*r) calculation for each radius given
        
        # print(areaOfFirstCircle, areaOfSecondCircle)
        # just to check if the values in the variables make sense
        
        # if-else statement to check which circle is the smaller circle
        if areaOfFirstCircle < areaOfSecondCircle: 
            totalAreaCovered = (areaOfFirstCircle / areaOfSecondCircle) * 100
        else:
            totalAreaCovered = (areaOfSecondCircle / areaOfFirstCircle) * 100
        
        return(f"{totalAreaCovered}%")
    except:
        return ("Invalid input, at least one radius given is a string.")
    
# example code:
# print(AreaCoveredBySmallerCircle(1.1, 2))