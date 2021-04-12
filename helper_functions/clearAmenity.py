# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:28:52 2021

@author: allst
"""
import pandas as pd 
import numpy as np
import collections as col
def join_main_category(new_category, sub_categories,word_dict,size,data):
    
    '''
        this function joins sub_categories into a main category
        ==============================================================
        input:
            - new_category   : name of the new main category 
              type           : string 
              
            - sub_categories : the names of the sub_categories to be joined 
              type           : list
              
            - word_dict      : the dictionary with all raw amenities
              type           : dict
            
            - size           : how many elements should have the np.array
              type           : int 
            
            - data           : our main data 
              type           : pd DataFrame
        **************************************************************      
        output:
            - category_exists: 1 if the category exists , 0 if not
              type = np.array 
        ==============================================================      
    '''
    name_of_category = new_category
    

    for amen in data["amenities"]:
        for list_item in amen:

            ind = amen.index(list_item)
            amen[ind] = amen[ind].replace(' \"','\"')


    category = pd.Series(sub_categories) 
                        # inside of the category belongs all the sub_categories

    myDict = col.defaultdict(list)
    for key in word_dict.keys():

        for cat in category:
            if (cat in key):
               myDict[name_of_category].append(str(key))

    # create a zeros np array

    myDict = dict(myDict)

    category_exists = np.zeros(size)
    key = name_of_category

    for ind in range(0,size):

        amenity = data.iloc[ind]["amenities"]

        for key, value in myDict.items(): # iterate in keys,values of myDict
            for val in value:

                if val in amenity:
                    # if the list contains the value , then set the key columns to 1 

                    category_exists[ind] = 1
                
    return category_exists