import pandas as pd
import statsmodels.api as sm

def Backward_Elimination(X,y):

    '''
        Input : The feature series for comparison and the target
        Output :  Returning the final set of features
    '''

    cols = list(X.columns)
    pmax = 1
    while (len(cols)>0):
        p= []
        X_1 = X[cols]
        X_1 = sm.add_constant(X_1)
        model = sm.OLS(y,X_1).fit()
        p = pd.Series(model.pvalues.values[1:],index = cols)
        pmax = max(p)
        feature_with_p_max = p.idxmax()
        # print(pmax)
        if(pmax>0.05):
            cols.remove(feature_with_p_max)
        else:
            break

    selected_features_BE = cols
    return selected_features_BE
