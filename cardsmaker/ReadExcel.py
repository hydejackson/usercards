#read in Excel file and create a dataframe object with pandas
#in:  filename
#out: DataFrame object

import pandas as pd

def readExcel(excelFileName):
    #open Excel file and read to dataframe
    df = pd.DataFrame(pd.read_excel(excelFileName))

    return(df)