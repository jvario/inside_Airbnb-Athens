import numpy as np
import pandas as pd

def fill_beds(df_row):
    """ input: dataframe
    fills nan values of beds with the values of "beds" from cells with the same value of "accommodates"
    output: dataframe with the column "beds" without nan"""

    if str(df_row["beds"]) == "nan" : 
        for i in range(0, int(df['accommodates'].max() + 1)) :
            if df_row["accommodates"] == i:
                data_temp = df[df["accommodates"] == i]
                df_row["beds"] = round(data_temp["beds"].mean())
    
    return df_row
