import pandas as pd
import numpy as np
import helper_functions.DataFrames as dfimport


def FillNaNWithCurrentDistribution(column, df):
    '''
        Input : The name of the column to witch the fillig strategy should be applied to, 
        plus the DataFrame object contanig the relevant data.

        Output :  The Pandas DataFrame object given as input. Containing the column where missing values have been supplanted,
        by values based on the current distibition.
    '''
    data = df

    # Current distribution, [dtype: float64]
    s = data[column].value_counts(normalize=True)
    missing = data[column].isnull()

    data.loc[missing, column] = np.random.choice(
        s.index, size=len(data[missing]), p=s.values)

    #res_ser = pd.Series(data[column])
    return data


def FillNaNWithCurrentDistributionFromCsv(column, csv):
    '''
        Input : The name of the column to witch the fillig strategy, for missing values, should be applied.
        Plus the csv name the data should obtained from.

        Output : A Pandas Series objected. Containing the column where missing values have been supplanted,
        by values based on the current distibition.
    '''
    data = pd.DataFrame()

    if csv.__eq__('listings.csv'):
        data = dfimport.GetListingsDataFrame()
    elif csv.__eq__('primary_data.csv'):
        data = dfimport.GetPrimaryDataFrame()
    elif csv.__eq__('secondary_data.csv'):
        data = dfimport.GetSecondaryDataFrame()
    else:
        raise Exception('No data set with this name could be found!')

    # Current distribution, [dtype: float64]
    s = data[column].value_counts(normalize=True)
    missing = data[column].isnull()

    data.loc[missing, column] = np.random.choice(
        s.index, size=len(data[missing]), p=s.values)

    res_ser = pd.Series(data[column])
    return res_ser
