#separate DataFrame into individual "rows"
#in:  pandas.DataFrame
#out: list [name, id]

import pandas as pd

def rowClass(df: pd.DataFrame):
    #loop through each row in the df and add it to a regular array
    rowsList = []
    fullList = df.to_dict()
    fullListValues = list(fullList.values())
    ids = fullListValues[0]
    names = fullListValues[1]
    for i in range(len(ids)):
        rowsList.append([names[i], ids[i]])

    return rowsList