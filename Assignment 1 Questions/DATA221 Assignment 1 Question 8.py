import pandas as pd

data = {
    "A": [1,2,3,1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

def printDataFrameFromData(data):
    # create the dataframe with pandas
    newDataFrame = pd.DataFrame(data)
    
    # create a new column from
    # dividing column B by column C, according to the documentation of pandas
    # (https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
    
    newDataFrame["C/A (rounded)"] = round(newDataFrame["C"] / newDataFrame["A"], 2) # round the quotient to 2 decimals
    
    print(newDataFrame)

printDataFrameFromData(data)