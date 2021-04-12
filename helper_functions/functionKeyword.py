#inputs : 1)series = a series with each row be a list of strings, 2) key = a string which is a keyword to search for                     
#return : a series with value 1 if the keyword was in the corresponding row of the input series, else 0
 
def keyword_in_series(series, key):
    list_keyword = []
    for row in series:
        i=0
        for j in row:
            if key in j:
                list_keyword.append(1)
                break
            else:
                i+=1
        if i == len(row):
            list_keyword.append(0)
    list_keyword = pd.Series(list_keyword)
    return list_keyword


