import pandas as pd
import numpy as np
from sklearn.cluster import KMeans


def clustering_neighbourhoods(clusters,clear_data ):
    '''
        Input : The number of clusters
        Output :  The dataframe of clustered labels
    '''

    total_data = pd.read_csv('data/listings.csv')
    # adding extra cols from total dataset
    neighbors = total_data[['neighbourhood_cleansed', 'latitude', 'longitude']]
    # one_hot_encoded neighbourhood_cleansed
    x = pd.get_dummies(neighbors.neighbourhood_cleansed, prefix='neighbourhood')
    # running cluster
    kmeans = KMeans(n_clusters=clusters, random_state=0).fit(x)
    neighbors.insert(0, 'Neighbourhood_CLabels', kmeans.labels_)
    # plot data with seaborn facet = sns.lmplot(data=neighbors, x='latitude', y='longitude',
    # hue='Neighbourhood_CLabels',fit_reg=False, legend=True, legend_out=True)
    clear_data.insert(0, 'Neighbourhood_CLabels', kmeans.labels_)
    # one-hot-encoded NLabels
    NLabels = pd.get_dummies(clear_data.Neighbourhood_CLabels, prefix='NLabels')
    clear_data = clear_data.join(NLabels)
    clear_data = clear_data.drop(['Neighbourhood_CLabels'], axis=1)
    return clear_data
