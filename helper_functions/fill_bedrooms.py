import numpy as np
import pandas as pd

def fill_bedrooms(df_row):
    """ input: dataframe
    fills nan values of bedrooms with the values of "bedrooms" from cells with the same value of "beds"
    output: dataframe with the column "bedrooms" without nan"""

    if str(df_row["bedrooms"]) == "nan" : 
        for i in range(0, int(df['beds'].max()+1)) :
            if df_row["beds"] == i:
                data_temp = df[df["beds"] == i]
                df_row["bedrooms"] = round(data_temp["bedrooms"].mean())
    
    return df_row
