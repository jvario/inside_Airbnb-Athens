'''
  input :
  
      drop  : condition for dropping or not nan // boolean 
      series: a series with values 't' and 'f'  // pandas series

  output :
      a series which is label encoded ('t' -> 1, 'f' -> 0)
'''
import pandas as pd
import numpy as np
def clean_t_f(series,drop):
    s = series.value_counts(normalize=True,dropna = drop)
    series_fill_na = series.fillna(pd.Series(np.random.choice(s.index, p=s.values, size=len(series.isnull()))))
    series_encoded = series_fill_na.replace({'f': 0, 't': 1})
    return series_encoded