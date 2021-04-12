import numpy as np
import pandas as pd
import helper_functions.DataFrames as dfimport
import helper_functions.FillNaNValues as fillna
from sklearn.preprocessing import LabelEncoder


def EncodingProcessOnGivenColumn(column, df):
    '''
        Input :  The name of the column, to witch label encoding should be performed,
        plus the DataFrame object contanig the relevant data.

        Output : The Pandas DataFrame object given as input, containing the encoded version of the data.
    '''
    # Copy data to new variable
    data = df

    # Create instance of labelencoder
    labelencoder = LabelEncoder()

    # Prepare data
    data[column] = fillna.FillNaNWithCurrentDistribution(column, df)

    # Assigning numerical values, calling the fit_transform method of the Label encoder.
    data[column] = labelencoder.fit_transform(data[column])

    return data[column]
