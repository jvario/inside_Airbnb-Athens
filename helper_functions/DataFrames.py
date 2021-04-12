import os
import pandas as pd


def GetListingsDataFrame():
    '''
        Input :  None
        Output : A pandas data frame, containing the records of the listings.csv
    '''

    listings_path = os.getcwd() + "/data/listings.csv"
    df = pd.read_csv(listings_path)
    return df


def GetPrimaryDataFrame():
    '''
        Input :  None
        Output : A pandas data frame, containing the records of the primary_data.csv
    '''

    primary_path = os.getcwd() + "/data/primary_data.csv"
    df = pd.read_csv(primary_path)
    return df


def GetSecondaryDataFrame():
    '''
        Input :  None
        Output : A pandas data frame, containing the records of the secondary_data.csv
    '''

    secondary_path = os.getcwd() + "/data/secondary_data.csv"
    df = pd.read_csv(secondary_path)
    return df
